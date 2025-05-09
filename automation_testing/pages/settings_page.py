# AmaderHR_Automation/pages/settings_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SettingsPage(BasePage):
    # --- Locators for WorkSlot Page (under Settings) ---
    WORKSLOT_PAGE_HEADER = (By.XPATH, "//h3[contains(text(),'WorkSlot')]") # Or a more unique element
    ADD_NEW_WORKSLOT_BUTTON = (By.XPATH, "//a[contains(text(),'Add New WorkSlot') or .//i[contains(@class, 'fa-plus')]]") # Adjust based on actual button
    WORKSLOT_TITLE_INPUT = (By.ID, "title") # Placeholder - Check actual ID/name
    WORKSLOT_START_TIME_INPUT = (By.ID, "start_time") # Placeholder
    WORKSLOT_END_TIME_INPUT = (By.ID, "end_time") # Placeholder
    WORKSLOT_LATE_COUNT_TIME_INPUT = (By.ID, "late_count_time") # Placeholder
    SAVE_WORKSLOT_BUTTON = (By.XPATH, "//button[@type='submit' and (contains(text(),'Save') or contains(text(),'Create'))]")
    WORKSLOT_TABLE = (By.ID, "workslotTable") # Placeholder for the table listing workslots
    SUCCESS_MESSAGE_GENERIC = (By.XPATH, "//div[contains(@class, 'alert-success') or contains(@class,'swal2-success-ring')]")


    def __init__(self, driver):
        super().__init__(driver)

    def is_workslot_page_visible(self):
        return self.is_element_visible(self.WORKSLOT_PAGE_HEADER)

    def click_add_new_workslot(self):
        self.do_click(self.ADD_NEW_WORKSLOT_BUTTON)

    def enter_workslot_details(self, title, start_time, end_time, late_time):
        self.do_send_keys(self.WORKSLOT_TITLE_INPUT, title)
        self.do_send_keys(self.WORKSLOT_START_TIME_INPUT, start_time)
        self.do_send_keys(self.WORKSLOT_END_TIME_INPUT, end_time)
        self.do_send_keys(self.WORKSLOT_LATE_COUNT_TIME_INPUT, late_time)
        # Add other fields if necessary (e.g., overtime options)

    def click_save_workslot(self):
        self.do_click(self.SAVE_WORKSLOT_BUTTON)

    def get_general_success_message(self):
        if self.is_element_visible(self.SUCCESS_MESSAGE_GENERIC):
            return self.get_element_text(self.SUCCESS_MESSAGE_GENERIC)
        return None

    def is_workslot_in_list(self, workslot_title):
        if not self.is_element_visible(self.WORKSLOT_TABLE):
            return False
        try:
            # Example: Find a cell containing the workslot_title text within the table
            # You'll need to inspect the actual table structure for a robust XPath
            workslot_cell = self.find_element((By.XPATH, f"//table[@id='{self.WORKSLOT_TABLE[1]}']//td[contains(text(), '{workslot_title}')]"))
            return workslot_cell.is_displayed()
        except:
            return False
