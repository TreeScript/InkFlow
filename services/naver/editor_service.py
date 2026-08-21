from playwright.sync_api import Page, FrameLocator, Locator

NAVER_BLOG_HOME_URL = "https://blog.naver.com"
NAVER_EDITOR_FRAME_SELECTOR = "iframe[name='mainFrame']"


def open_blog_home(page: Page) -> None:
    page.goto(
        NAVER_BLOG_HOME_URL,
        wait_until = "domcontentloaded"
    )
    
    

def open_blog_editor(page: Page) -> None:
    open_blog_home(page = page)
    
    write_link = page.get_by_role(
        "link",
        name = "글쓰기"
    )
    
    with page.context.expect_page() as new_page_info:
        write_link.click()
    
    editor_page = new_page_info.value
    editor_page.wait_for_load_state(
        "domcontentloaded"
    )
    
    return editor_page
    
    

def get_blog_editor_frame(page: Page) -> FrameLocator:
    return page.frame_locator(
        NAVER_EDITOR_FRAME_SELECTOR
    )
    
    

def get_title_locator(page: Page) -> Locator:
    frame = get_blog_editor_frame(page = page)
    
    return frame.get_by_role("paragraph").filter(has_text = "제목")



def input_blog_title(page: Page, title: str) -> None:
    title = title.strip()
    if not title:
        raise ValueError("블로그 제목이 비어 있습니다.")
    
    title_locator = get_title_locator(page = page)
    title_locator.click()
    
    page.keyboard.insert_text(title)