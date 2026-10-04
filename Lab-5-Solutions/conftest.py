import os
import sys
from pathlib import Path
import pytest
from selenium import webdriver

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


@pytest.fixture
def browser(request):
    os.environ.setdefault("SE_TIMEOUT", "30")
    options = webdriver.ChromeOptions()
    remote = os.environ.get("LAB5_REMOTE_URL")
    driver = (webdriver.Remote(command_executor=remote, options=options)
              if remote else webdriver.Chrome(options=options))
    try:
        driver.set_window_size(1280, 900)
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(2)
        default_url = ("http://host.docker.internal:8010/demo_page.html" if remote
                       else "http://localhost:8010/demo_page.html")
        driver.get(os.environ.get("LAB5_BASE_URL", default_url))
        yield driver
    finally:
        # Captures actual page state after each test, including a failed assertion.
        directory = ROOT / "reports" / os.environ.get("LAB5_PHASE", "direct") / "screenshots"
        directory.mkdir(parents=True, exist_ok=True)
        name = request.node.callspec.id if hasattr(request.node, "callspec") else request.node.name
        try:
            driver.save_screenshot(str(directory / f"{name}.png"))
        finally:
            driver.quit()
