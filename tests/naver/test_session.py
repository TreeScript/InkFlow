from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    input_naver_account,
    is_logged_in,
    login_naver,
)


def test_naver_session() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(
            playwright=playwright
        )

        page = context.pages[0]

        if is_logged_in(page):
            print()
            print("기존 네이버 로그인 세션을 확인했습니다.")

        else:
            print()
            print("저장된 로그인 세션이 없습니다.")

            account = input_naver_account()

            login_naver(
                page=page,
                account=account
            )

            print()
            print(
                "로그인을 요청했습니다. "
                "추가 인증이 있다면 브라우저에서 직접 처리해주세요."
            )

            input(
                "로그인을 완료한 뒤 Enter를 눌러주세요..."
            )

            if is_logged_in(page):
                print()
                print("네이버 로그인 성공 및 세션 저장 확인")

            else:
                print()
                print("로그인 상태를 확인하지 못했습니다.")

        input(
            "테스트를 종료하려면 Enter를 눌러주세요..."
        )

        context.close()


if __name__ == "__main__":
    test_naver_session()