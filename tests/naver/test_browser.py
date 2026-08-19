from playwright.sync_api import sync_playwright

def test_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless = False
        )
        
        page = browser.new_page()
        page.goto(
            "https://www.naver.com",
            wait_until = "domcontentloaded"
        )
        
        print("브라우저 실행 및 네이버 접속 성공")
        input("확인했으면 Enter를 눌러 브라우저를 종료하세요...")
        
        browser.close()
        
if __name__ == "__main__":
    test_browser()