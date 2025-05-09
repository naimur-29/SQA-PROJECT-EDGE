# tests/conftest.py
import datetime
import os

import pytest
import pytest_html  # Import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.config import BASE_URL, IMPLICIT_WAIT_TIME, SCREENSHOT_DIR
from webdriver_manager.chrome import ChromeDriverManager

# Ensure screenshot directory exists
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

@pytest.fixture(scope="session")
def driver():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    service = ChromeService(executable_path=ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service, options=chrome_options)
    web_driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    yield web_driver
    web_driver.quit()

# Hook to add environment info to HTML report
def pytest_configure(config):
    # For newer versions of pytest-html, directly modifying _metadata might not be available
    # or might behave differently. Using config.stash is a more robust way.
    if not hasattr(config, 'stash'):
        config.stash = {} # Initialize if it doesn't exist
    if 'environment' not in config.stash:
        config.stash['environment'] = [] # Ensure 'environment' list exists in stash

    # Add your custom metadata to the 'environment' list in stash
    # pytest-html will pick this up for the Environment table
    config.stash['environment'].append(('Project Name', 'AmaderHR'))
    config.stash['environment'].append(('Module', 'Salary, Rosters, Attendance'))
    config.stash['environment'].append(('Tester', 'SQA Final Project Student'))
    config.stash['environment'].append(('Base URL', BASE_URL))

# Hook to take screenshot on test failure and embed in HTML report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call':
        if report.failed and "driver" in item.fixturenames:
            driver_instance = item.funcargs["driver"]
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            # Ensure item.name is filesystem-friendly
            test_name = "".join(c if c.isalnum() else "_" for c in item.name)
            screenshot_name = f"{SCREENSHOT_DIR}{test_name}_{timestamp}.png"
            try:
                driver_instance.save_screenshot(screenshot_name)
                with open(screenshot_name, "rb") as image_file:
                    import base64
                    encoded_string = base64.b64encode(image_file.read()).decode()
                html = f'<div><p>Screenshot:</p><img src="data:image/png;base64,{encoded_string}" alt="screenshot" style="width:600px;"/></div>'
                extras.append(pytest_html.extras.html(html))
            except Exception as e:
                print(f"Error taking or embedding screenshot: {e}")
        report.extras = extras
