from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    ensure_naver_login,
    input_blog_title,
    input_heading_block,
    input_body_text,
    open_blog_editor,
)


def test_heading_block() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        ensure_naver_login(page=page)

        editor_page = open_blog_editor(page=page)

        input_blog_title(
            page=editor_page,
            title="HeadingBlock 테스트",
        )

        input_heading_block(
            page=editor_page,
            content="여의도의 시작",
        )

        input_body_text(
            page=editor_page,
            content="""
                여의도는 한강 가운데 위치했던 섬에서 시작되었습니다.

                이 문단은 Heading 아래에 들어가는 일반 본문입니다.
            """.strip(),
        )

        print("Heading 테스트 완료")

        editor_page.pause()

        context.close()


if __name__ == "__main__":
    test_heading_block()