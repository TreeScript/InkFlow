from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    ensure_naver_login,
    input_blog_title,
    open_blog_editor,
)


TEST_TITLE = "InkFlow 네이버 블로그 제목 자동 입력 테스트"


def test_title_input() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        ensure_naver_login(
            page=page
        )

        editor_page = open_blog_editor(
            page=page
        )

        input_blog_title(
            page=editor_page,
            title=TEST_TITLE,
        )

        print()
        print("제목 입력 완료")
        editor_page.pause()

        context.close()


if __name__ == "__main__":
    test_title_input()