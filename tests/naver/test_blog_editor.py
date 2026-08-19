from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    ensure_naver_login,
    open_blog_home,
)


def test_blog_editor() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        ensure_naver_login(
            page=page
        )

        print()
        print("네이버 로그인 확인 완료")

        open_blog_home(
            page=page
        )

        print("네이버 블로그 페이지 이동 완료")
        print()
        print(f"현재 URL: {page.url}")

        input(
            "블로그 화면을 확인한 뒤 Enter를 눌러주세요..."
        )

        context.close()


if __name__ == "__main__":
    test_blog_editor()