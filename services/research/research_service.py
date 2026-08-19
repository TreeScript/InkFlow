from openai import OpenAI

from config.settings import OPENAI_MODEL
from models.research import ResearchData, ResearchSource
from prompts.research import build_research_prompt
from .source_service import (create_research_source, sort_sources)


def extract_sources(response) -> list[ResearchSource]:
    sources: list[ResearchSource] = []
    seen_urls: set[str] = set()

    for output_item in response.output:
        if output_item.type != "web_search_call":
            continue

        output_data = output_item.model_dump()

        action = output_data.get("action")
        if not action:
            continue

        if action.get("type") != "search":
            continue

        source_items = action.get("sources") or []

        for source in source_items:
            url = source.get("url", "").strip()

            if not url:
                continue

            if url in seen_urls:
                continue

            seen_urls.add(url)

            sources.append(
                create_research_source(
                    url=url
                )
            )

    return sort_sources(sources)


def search_research_material(
    client: OpenAI,
    topic: str
):
    prompt = build_research_prompt(topic)

    return client.responses.create(
        model=OPENAI_MODEL,
        tools=[
            {
                "type": "web_search",
                "search_context_size": "high"
            }
        ],
        tool_choice="auto",
        include=[
            "web_search_call.action.sources"
        ],
        input=prompt
    )


def structure_research_data(
    client: OpenAI,
    topic: str,
    raw_report: str,
    sources: list[ResearchSource]
) -> ResearchData:
    source_urls = "\n".join(
        source.url
        for source in sources
    )

    prompt = f"""
다음 웹 조사 결과를 분석하여 ResearchData 구조로 정리해주세요.

사용자 주제:
{topic}

웹 조사 결과:
{raw_report}

참고한 출처:
{source_urls}

작성 원칙:
- 웹 조사 결과에 포함되지 않은 사실을 임의로 추가하지 마세요.
- 핵심 사실은 key_facts에 정리해주세요.
- 시간 순서가 중요하다면 timeline에 정리해주세요.
- 의미 있는 수치가 있다면 statistics에 정리해주세요.
- 자료가 부족한 항목은 억지로 채우지 말고 빈 배열로 두세요.
""".strip()

    response = client.responses.parse(
        model=OPENAI_MODEL,
        input=prompt,
        text_format=ResearchData
    )

    research_data = response.output_parsed

    if research_data is None:
        raise RuntimeError(
            "ResearchData 구조화에 실패했습니다."
        )

    research_data.topic = topic
    research_data.sources = sources

    return research_data


def research_topic(
    client: OpenAI,
    topic: str
) -> ResearchData:
    search_response = search_research_material(
        client=client,
        topic=topic
    )

    raw_report = search_response.output_text

    if not raw_report.strip():
        raise RuntimeError(
            "웹 검색 결과에서 조사 내용을 가져오지 못했습니다."
        )

    sources = extract_sources(
        search_response
    )

    # print(
    #     f"웹 검색 결과: "
    #     f"{len(sources)}개 고유 출처 수집"
    # )
    
    # for source in sources[:10]:
    #     print(
    #         f"[P{source.priority}] "
    #         f"{source.source_type:<10}"
    #         f"{source.domain}"
    #     )

    return structure_research_data(
        client=client,
        topic=topic,
        raw_report=raw_report,
        sources=sources
    )