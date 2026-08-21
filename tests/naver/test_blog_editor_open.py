from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    ensure_naver_login,
    open_blog_editor,
)


def test_blog_editor_open() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        ensure_naver_login(page=page)

        editor_page = open_blog_editor(page = page)

        print()
        print("네이버 블로그 글쓰기 화면 진입 완료")
        print(
            f"Editor URL: "
            f"{editor_page.url}"
        )
        
        editor_page.pause()
        context.close()


if __name__ == "__main__":
    test_blog_editor_open()