from playwright.sync_api import Page, FrameLocator, Locator
from enum import Enum

class ParagraphStyle(str, Enum):
    BODY = "본문"
    HEADING = "소제목"
    QUOTE = "인용구"

NAVER_BLOG_HOME_URL = "https://blog.naver.com"
NAVER_EDITOR_FRAME_SELECTOR = "iframe[name='mainFrame']"


def open_blog_home(page: Page) -> None:
    page.goto(
        NAVER_BLOG_HOME_URL,
        wait_until = "domcontentloaded"
    )
    
    

def open_blog_editor(page: Page) -> Page:
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


def get_body_locator(page: Page) -> Locator:
    frame = get_blog_editor_frame(page = page)
    
    return frame.get_by_role("paragraph").filter(has_text = "나를 돌아보는 회고, 뜻밖의 발견을 기다립니다. #모두의회고")


def input_body_text(page: Page, content: str) -> None:
    content = content.strip()
    if not content:
        raise ValueError("블로그 본문이 비어있습니다.")
    
    body_locator = get_body_locator(page = page)
    body_locator.click()
    
    lines = content.split("\n")
    
    for index, line in enumerate(lines):
        if line:
            page.keyboard.insert_text(line)
            
        if index < len(lines) - 1:
            page.keyboard.press("Enter")


def select_paragraph_style(page: Page, style: ParagraphStyle) -> None:
    frame = get_blog_editor_frame(page = page)
    frame.get_by_role(
        "button",
        name = "문단 서식 변경"
    ).click()
    
    frame.get_by_role(
        "button",
        name = style.value,
        exact = True
    ).click()
    
    
def input_heading_block(page: Page, content: str) -> None:
    content = content.strip()
    if not content:
        raise ValueError("Heading 내용이 비어 있습니다.")
    
    body = get_body_locator(page = page)
    body.click()
    
    page.keyboard.insert_text(content)
    
    select_paragraph_style(page = page, style = ParagraphStyle.HEADING)
    page.keyboard.press("Enter")
    
    select_paragraph_style(page = page, style = ParagraphStyle.BODY)