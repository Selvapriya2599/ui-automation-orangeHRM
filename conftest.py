import pytest
from playwright.sync_api import sync_playwright
from config import BASE_URL
from pages.loginPage import LoginPage
import os 
import json

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright
 
@pytest.fixture(scope="session")       
def get_browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)    
    yield browser
    browser.close()
  
@pytest.fixture(scope="session")    
def get_context(get_browser):
    context = get_browser.new_context()        
    yield context
    context.close()
 
@pytest.fixture(scope="session")     
def get_page(get_context):
    page = get_context.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()
   
@pytest.fixture(scope="session")    
def payload() ->  dict:
    path = os.path.join(os.path.dirname(__file__),"data","payload.json")
    with open(path, "r") as f:
        payload = json.load(f)
        return payload
    
@pytest.fixture(scope="function")
def loginPage(get_page):
    return LoginPage(get_page)

@pytest.fixture(scope="session")
def wrong_credentials(payload) -> dict:
    return payload["wrong_crdentials"]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("get_page") 
        if page:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            filename = f"{report.nodeid.replace('::','_')}_{report.outcome}.png"
            filepath = os.path.join(screenshots_dir, filename)

            page.screenshot(path=filepath)
            print(f"Screenshot saved: {filepath}")