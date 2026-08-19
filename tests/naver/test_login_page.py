from playwright.sync_api import sync_playwright
from services.naver import create_browser_context


NAVER_LOGIN_URL = "https://nid.naver.com/nidlogin.login"


def test_naver_login_page() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(playwright = playwright)
        
        page = context.pages[0]
        page.goto(
            NAVER_LOGIN_URL,
            wait_until = "domcontentloaded"
        )
        
        print("네이버 로그인 페이지 이동 완료")
        
        input("로그인 화면이 정상적으로 보이면 Enter를 눌러 종료하세요...")
        
        context.close()
        
if __name__ == "__main__":
    test_naver_login_page()