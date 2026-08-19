from getpass import getpass
from playwright.sync_api import Page
from models.naver import NaverAccount

NAVER_LOGIN_URL = "https://www.naver.com"

def input_naver_account() -> NaverAccount:
    print()
    print("=" * 50)
    print("네이버 로그인")
    print("=" * 50)
    
    login_id = input(
        "네이버 아이디: "
    ).strip()
    if not login_id:
        raise ValueError(
            "네이버 아이디를 입력해주세요."
        )
        
    password = getpass(
        "네이버 비밀번호: "
    )
    if not password:
        raise ValueError(
            "네이버 비밀번호를 입력해주세요."
        )
        
    return NaverAccount(
        login_id = login_id,
        password = password
    )
    

def open_naver_login_page(page: Page) -> None:
    page.goto(
        NAVER_LOGIN_URL,
        wait_until = "domcontentloaded"
    )
    

def fill_naver_login_form(page: Page, account: NaverAccount) -> None:
    page.locator('#id').fill(account.login_id)
    
    page.locator('#pw').fill(account.password)
    

def submit_naver_login(page: Page) -> None:
    page.get_by_role(
        "button",
        name = "로그인"    
    ).click()
    
    
def login_naver(page: Page, account: NaverAccount) -> None:
    open_naver_login_page(page = page)
    
    fill_naver_login_form(page = page, account = account)
    
    submit_naver_login(page = page)
    
    
def is_logged_in(page: Page) -> bool:
    page.goto(
        "https://www.naver.com",
        wait_until = "domcontentloaded"
    )
    
    login_button = page.get_by_role(
        "link",
        name = "NAVER 로그인"
    )
    
    return login_button.count() == 0


def ensure_naver_login(page: Page) -> None:
    if is_logged_in(page):
        print("기존 네이버 로그인 세션을 확인했습니다.")
        return
    
    print()
    print("네이버 로그인이 필요합니다.")
    print("브라우저에서 직접 로그인해주세요.")
    print("추가 인증이 나오면 직접 처리해주세요.")
    
    open_naver_login_page(page = page)
    
    input("로그인을 완료한 뒤 Enter를 눌러주세요...")
    
    if not is_logged_in(page):
        raise RuntimeError("네이버 로그인 상태를 확인하지 못 했습니다.")
    
    print("네이버 로그인 상태 확인 완료")