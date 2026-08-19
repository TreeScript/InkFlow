from pathlib import Path
from playwright.sync_api import BrowserContext, Playwright


BASE_DIR = Path(__file__).resolve().parents[2]
BROWSER_DATA_DIR = BASE_DIR / "data" / "browser"


def create_browser_context(playwright: Playwright) -> BrowserContext:
    BROWSER_DATA_DIR.mkdir(
        parents = True,
        exist_ok = True
    )
    
    return playwright.chromium.launch_persistent_context(
        user_data_dir = str(BROWSER_DATA_DIR),
        channel = "chrome",
        headless = False,
        chromium_sandbox = True,
        ignore_https_errors = True
    )