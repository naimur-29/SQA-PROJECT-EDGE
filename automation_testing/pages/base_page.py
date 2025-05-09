# pages/base_page.py
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.config import EXPLICIT_WAIT_TIME


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_title(self, title):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.title_is(title))
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover_over_element_and_click(self, hover_locator, click_locator):
        actions = ActionChains(self.driver)
        hover_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(hover_locator))
        actions.move_to_element(hover_element).perform()
        click_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.element_to_be_clickable(click_locator))
        click_element.click()

    def select_dropdown_by_visible_text(self, by_locator, text):
        from selenium.webdriver.support.ui import Select
        select_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_dropdown_by_value(self, by_locator, value):
        from selenium.webdriver.support.ui import Select
        select_element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
        select = Select(select_element)
        select.select_by_value(value)

    def wait_for_element_to_be_clickable(self, by_locator):
        return WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.element_to_be_clickable(by_locator))
    
    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of(element)) # Ensure it's visible after scroll

    def switch_to_frame(self, frame_locator):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def accept_alert(self):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_alert_text(self):
        WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert.text

    def find_element(self, by_locator):
        return WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))

    def find_elements(self, by_locator):
        return WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_all_elements_located(by_locator))
