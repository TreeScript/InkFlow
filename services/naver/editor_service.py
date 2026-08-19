from playwright.sync_api import Page

NAVER_BLOG_HOME_URL = "https://blog.naver.com"


def open_blog_home(page: Page) -> None:
    page.goto(
        NAVER_BLOG_HOME_URL,
        wait_until = "domcontentloaded"
    )