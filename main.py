from models.blog_post import BlogPost
from models.content_block import ContentBlock
from services.research_service import research_topic
from services.openai_service import create_openai_client, generate_blog_post
from services.content_plan_service import create_content_plan


def get_topic() -> str:
    return input("블로그 주제를 입력하세요: ").strip()


def print_block(block: ContentBlock) -> None:
    if block.type == "text":
        print(block.content)
        print()
        return

    if block.type == "heading":
        prefix = "#" if block.level == 1 else "##"

        print(f"\n{prefix} {block.content}")
        print()
        return

    if block.type == "bullet_list":
        for item in block.items:
            print(f"• {item}")

        print()
        return

    if block.type == "numbered_list":
        for index, item in enumerate(block.items, start=1):
            print(f"{index}. {item}")

        print()
        return

    if block.type == "quote":
        print(f"> {block.content}")
        print()
        return

    if block.type == "divider":
        print("-" * 60)
        print()
        return

    if block.type == "image":
        print("[IMAGE]")
        print(f"검색어: {block.query}")
        print(f"캡션: {block.caption}")
        print()
        return

    if block.type == "video":
        print("[VIDEO]")
        print(f"검색어: {block.query}")
        print(f"캡션: {block.caption}")
        print()
        return

    if block.type == "link":
        print("[LINK]")
        print(f"{block.title}: {block.url}")
        print()
        return

    if block.type == "place":
        print("[PLACE]")
        print(f"장소: {block.name}")
        print(f"주소: {block.address}")
        print(f"설명: {block.description}")
        print()


def print_research_data(research_data) -> None:
    print()
    print("=" * 80)
    print("[RESEARCH DEBUG]")
    print("=" * 80)
    
    print()
    print("[SUMMARY]")
    print(research_data.summary)
    
    print()
    print("[KEY FACTS]")
    
    if research_data.key_facts:
        for index, fact in enumerate(research_data.key_facts, start = 1):
            print(f"{index}. {fact.fact}")
            
            if fact.context:
                print(f"    → {fact.context}")
                if(fact.context):
                    print(f"    →{fact.context}")
    else:
        print("없음")                
        
    print()
    print("[TIMELINE]")
    
    if research_data.timeline:
        for item in research_data.timeline:
            print(
                f" - {item.period}"
                f"{item.event}"
            )
    else:
        print("없음")
        
    print()
    print("[STATISTICS]")
    
    if research_data.statistics:
        for statistic in research_data.statistics:
            print(
                f" - {statistic.label}"
                f"{statistic.value}"
            )
            
            if statistic.context:
                print(f"    →{statistic.context}")
    else:
        print("없음")
        
    print()
    print("[SOURCES]")
    
    if research_data.sources:
        for index, source in enumerate(
            research_data.sources,
            start=1
        ):
            print(f"{index}. {source.url}")
    else:
        print("없음")

    print("=" * 80)
    print()


def print_blog_post(blog_post: BlogPost) -> None:
    print()
    print("=" * 80)
    print(f"제목: {blog_post.title}")
    print(f"콘텐츠 유형: {blog_post.content_type}")
    print(f"톤: {blog_post.tone}")
    print("=" * 80)
    print()

    for block in blog_post.blocks:
        print_block(block)

    print("=" * 80)
    print("[태그]")
    print(", ".join(blog_post.tags))
    print("=" * 80)


def main() -> None:
    topic = get_topic()
    if not topic:
        print("주제가 입력되지 않았습니다.")
        return

    client = create_openai_client()
    
    print("\n관련 자료를 조사하고 있습니다...\n")
    research_data = research_topic(
        client = client,
        topic = topic
    )
    print(
        f"자료 조사 완료 "
        f"({len(research_data.sources)}개 출처 확인)"
    )
    
    print_research_data(research_data)
    
    content_plan = create_content_plan(
        client = client,
        topic = topic,
        research_data = research_data
    )
    print(
        f"컨텐츠 기획 완료 "
        f"({len(content_plan.sections)}개 섹션 / "
        f"depth: {content_plan.depth})"
    )

    print("\n블로그 콘텐츠를 구성하고 있습니다...\n")
    blog_post = generate_blog_post(
        client = client,
        topic = topic,
        research_data = research_data,
        content_plan = content_plan
    )

    print_blog_post(blog_post)


if __name__ == "__main__":
    main()