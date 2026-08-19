from playwright.sync_api import sync_playwright
from services.naver import create_browser_context


def test_session_init() -> None:
    with sync_playwright() as playwright:
        context = create_browser_context(playwright = playwright)
        
        page = context.pages[0]
        page.goto(
            "https://www.naver.com",
            wait_until = "domcontentloaded"
        )
        
        print()
        print("브라우저에서 네이버 로그인을 직접 완료해주세요.")
        print("추가 인증이 나오면 직접 처리해주세요.")
        
        input(
            "로그인이 완전히 끝난 뒤 Enter를 눌러주세요..."
        )
        
        context.close()
        
if __name__ == "__main__":
    test_session_init()