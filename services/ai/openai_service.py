from openai import OpenAI

from config.settings import OPENAI_MODEL, get_openai_api_key
from models.blog import BlogPost
from models.planning import ContentPlan
from models.research import ResearchData
from prompts.blog import build_blog_prompt


def create_openai_client() -> OpenAI:
    return OpenAI(
        api_key=get_openai_api_key()
    )


def generate_blog_post(
    client: OpenAI,
    topic: str,
    research_data: ResearchData,
    content_plan: ContentPlan
) -> BlogPost:
    prompt = build_blog_prompt(
        topic=topic,
        research_data=research_data,
        content_plan=content_plan
    )

    response = client.responses.parse(
        model=OPENAI_MODEL,
        input=prompt,
        text_format=BlogPost
    )

    blog_post = response.output_parsed

    if blog_post is None:
        raise RuntimeError(
            "OpenAI 응답을 BlogPost 형식으로 변환하지 못했습니다."
        )

    return blog_post