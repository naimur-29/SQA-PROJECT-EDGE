# pages/login_page.py
import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.config import ADMIN_PASSWORD, ADMIN_USERNAME, BASE_URL, LOGIN_URL


class LoginPage(BasePage):
    # Locators - These are guesses. Update them!
    USERNAME_INPUT = (By.NAME, "email") # Assuming name is 'email' for username
    PASSWORD_INPUT = (By.NAME, "password") # Assuming name is 'password'
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']") # Generic submit button
    DASHBOARD_WELCOME_TEXT = (By.XPATH, "//h2[contains(text(),'AmaderHR')]") # On the main page after login

    def __init__(self, driver):
        super().__init__(driver)
        # The login URL might be different, adjust if needed
        # For this demo, if BASE_URL is the login page, this is fine.
        # Otherwise, use config.LOGIN_URL
        self.driver.get(LOGIN_URL)
        time.sleep(2)


    def enter_username(self, username):
        self.do_send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.do_send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)

    def login(self, username=ADMIN_USERNAME, password=ADMIN_PASSWORD):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        # Wait for a known element on the dashboard to ensure login was successful
        return self.is_element_visible(self.DASHBOARD_WELCOME_TEXT)

    def get_login_error_message(self):
        # Locator for error message - highly dependent on actual implementation
        ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-danger') or contains(@class, 'error-message')]")
        if self.is_element_visible(ERROR_MESSAGE):
            return self.get_element_text(ERROR_MESSAGE)
        return None
