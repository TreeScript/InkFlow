from playwright.sync_api import sync_playwright

from services.naver import (
    create_browser_context,
    ensure_naver_login,
    input_blog_title,
    open_blog_editor,
    input_body_text
)


TEST_TITLE = "InkFlow 네이버 블로그 제목 자동 입력 테스트"

TEST_CONTENT = """
안녕하세요.

이 글은 InkFlow에서 Playwright를 이용해 자동으로 입력한 테스트 본문입니다.

현재 네이버 SmartEditor의 본문 입력 기능을 개발하고 있습니다.

본문이 정상적으로 입력된다면 다음 단계에서는 여러 개의 ContentBlock을 순서대로 입력하는 기능을 구현할 예정입니다.
테스트테스트테스트
""".strip()

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
        
        input_body_text(
            page = editor_page,
            content = TEST_CONTENT
        )

        print()
        print("제목 입력 완료")
        editor_page.pause()

        context.close()



if __name__ == "__main__":
    test_title_input()