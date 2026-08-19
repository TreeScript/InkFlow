from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    input_naver_account,
    login_naver,
)


def test_naver_login() -> None:
    account = input_naver_account()

    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        login_naver(
            page=page,
            account=account
        )

        print()
        print("로그인 요청을 완료했습니다.")
        print(
            "추가 인증이나 보안 확인이 표시되면 "
            "브라우저에서 직접 처리해주세요."
        )

        input(
            "로그인 상태를 확인한 뒤 Enter를 눌러 종료하세요..."
        )

        context.close()


if __name__ == "__main__":
    test_naver_login()