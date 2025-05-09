# pages/attendance_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AttendancePage(BasePage):
    # Locators for Online Attendance Page
    ONLINE_ATTENDANCE_TABLE = (By.ID, "leaveRequestToAdmin") # From site.txt, seems table ID is reused
    APPROVE_BUTTON_GENERIC = (By.XPATH, "//a[contains(@class, 'btn-success') and contains(text(),'Approve')]") # Example

    # Locators for Devices Page
    ADD_NEW_DEVICE_BUTTON = (By.XPATH, "//a[contains(text(),'Add New Device')]") # This is a common pattern
    DEVICE_NAME_INPUT = (By.ID, "name") # Assuming 'name' as ID, CHECK THIS
    DEVICE_IP_INPUT = (By.ID, "ip_address") # CHECK THIS
    DEVICE_PORT_INPUT = (By.ID, "port") # CHECK THIS
    SAVE_DEVICE_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(),'Save')]") # CHECK THIS
    DEVICE_TABLE = (By.ID, "deviceTable") # GUESS, CHECK THIS
    SUCCESS_MESSAGE_ALERT = (By.XPATH, "//div[contains(@class, 'alert-success')]") # Common pattern


    def __init__(self, driver):
        super().__init__(driver)

    def is_online_attendance_table_visible(self):
        return self.is_element_visible(self.ONLINE_ATTENDANCE_TABLE)

    def click_add_new_device(self):
        self.do_click(self.ADD_NEW_DEVICE_BUTTON)

    def enter_device_details(self, name, ip, port):
        self.do_send_keys(self.DEVICE_NAME_INPUT, name)
        self.do_send_keys(self.DEVICE_IP_INPUT, ip)
        self.do_send_keys(self.DEVICE_PORT_INPUT, port)

    def click_save_device(self):
        self.do_click(self.SAVE_DEVICE_BUTTON)

    def get_success_message(self):
        if self.is_element_visible(self.SUCCESS_MESSAGE_ALERT):
            return self.get_element_text(self.SUCCESS_MESSAGE_ALERT)
        return None

    def is_device_in_table(self, device_name):
        # This would require iterating through table rows, more complex
        # For now, a simple check if the table is visible
        if not self.is_element_visible(self.DEVICE_TABLE):
            return False
        try:
            device_row = self.find_element((By.XPATH, f"//table[@id='{self.DEVICE_TABLE[1]}']//td[contains(text(), '{device_name}')]"))
            return device_row.is_displayed()
        except:
            return False
