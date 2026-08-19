from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    ensure_naver_login,
)


def test_ensure_login() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        ensure_naver_login(
            page=page
        )

        print()
        print("네이버 인증 준비 완료")

        input(
            "테스트를 종료하려면 Enter를 눌러주세요..."
        )

        context.close()


if __name__ == "__main__":
    test_ensure_login()