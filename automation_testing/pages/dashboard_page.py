# pages/dashboard_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    # Main Navigation Locators (Guesses based on site.txt structure)
    # These XPath locators try to find menu items by the text they contain.
    # More robust locators (like specific IDs if available) are preferred.

    ATTENDANCE_MENU_LINK = (By.XPATH, "//span[text()='Attendance']/parent::a/parent::span/parent::a") # More specific due to nested spans
    ONLINE_ATTENDANCE_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/attendance/requested-online-attendances') and .//span[text()='Online Attendance']]")
    DAILY_ATTENDANCE_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/attendance/daily-attendance') and .//span[text()='Daily Attendance']]")
    DEVICES_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/zkteco-device') and .//span[text()='Devices']]")

    ROSTERS_MENU_LINK = (By.XPATH, "//span[text()='Rosters']/parent::a/parent::span/parent::a")
    EMPLOYEE_ROSTER_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/rosters?type=employee') and .//span[text()='Employee']]")
    DEPARTMENT_ROSTER_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/rosters?type=department') and .//span[text()='Department']]")

    SALARY_MENU_LINK = (By.XPATH, "//span[text()='Salary']/parent::a/parent::span/parent::a")
    PREPARE_SALARY_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/salary/prepare-salary') and .//span[text()='Prepare Salary']]")
    SALARY_LIST_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/salary/view-salary') and .//span[text()='Salary List']]")
    BONUS_SETTINGS_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/bonus') and .//span[text()='Bonus Settings']]")
    GENERATE_BONUS_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/user-bonus') and .//span[text()='Generate Bonus']]")

    SETTINGS_MENU_LINK = (By.XPATH, "//span[text()='Settings']/parent::a/parent::span/parent::a")
    WORKSLOT_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/work-slot') and .//span[text()='WorkSlot']]")
    
    PAYGRADE_MENU_LINK = (By.XPATH, "//span[text()='Pay Grade Management']/parent::a/parent::span/parent::a")
    GRADES_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/paygrade') and .//span[text()='Grades']]")
    EARNING_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/earning') and .//span[text()='Earning']]")
    DEDUCTION_SUBMENU_LINK = (By.XPATH, "//a[contains(@href, '/deduction') and .//span[text()='Deduction']]")

    ONLINE_CHECK_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Online Check In')]")
    ONLINE_CHECK_OUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Online Check Out')]") # Guessed locator
    DASHBOARD_TITLE = (By.XPATH, "//h2[text()='AmaderHR']") # To verify page load


    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_visible(self):
        return self.is_element_visible(self.DASHBOARD_TITLE)

    def navigate_to_online_attendance(self):
        self.hover_over_element_and_click(self.ATTENDANCE_MENU_LINK, self.ONLINE_ATTENDANCE_SUBMENU_LINK)

    def navigate_to_daily_attendance(self):
        self.hover_over_element_and_click(self.ATTENDANCE_MENU_LINK, self.DAILY_ATTENDANCE_SUBMENU_LINK)
    
    def navigate_to_devices(self):
        self.hover_over_element_and_click(self.ATTENDANCE_MENU_LINK, self.DEVICES_SUBMENU_LINK)

    def navigate_to_employee_roster(self):
        self.hover_over_element_and_click(self.ROSTERS_MENU_LINK, self.EMPLOYEE_ROSTER_SUBMENU_LINK)

    def navigate_to_department_roster(self):
        self.hover_over_element_and_click(self.ROSTERS_MENU_LINK, self.DEPARTMENT_ROSTER_SUBMENU_LINK)

    def navigate_to_prepare_salary(self):
        self.hover_over_element_and_click(self.SALARY_MENU_LINK, self.PREPARE_SALARY_SUBMENU_LINK)

    def navigate_to_salary_list(self):
        self.hover_over_element_and_click(self.SALARY_MENU_LINK, self.SALARY_LIST_SUBMENU_LINK)
    
    def navigate_to_bonus_settings(self):
        self.hover_over_element_and_click(self.SALARY_MENU_LINK, self.BONUS_SETTINGS_SUBMENU_LINK)

    def navigate_to_generate_bonus(self):
        self.hover_over_element_and_click(self.SALARY_MENU_LINK, self.GENERATE_BONUS_SUBMENU_LINK)

    def navigate_to_workslot_settings(self):
        self.hover_over_element_and_click(self.SETTINGS_MENU_LINK, self.WORKSLOT_SUBMENU_LINK)

    def navigate_to_pay_grades(self):
        self.hover_over_element_and_click(self.PAYGRADE_MENU_LINK, self.GRADES_SUBMENU_LINK)

    def navigate_to_pay_earnings(self):
        self.hover_over_element_and_click(self.PAYGRADE_MENU_LINK, self.EARNING_SUBMENU_LINK)

    def navigate_to_pay_deductions(self):
        self.hover_over_element_and_click(self.PAYGRADE_MENU_LINK, self.DEDUCTION_SUBMENU_LINK)
        
    def click_online_check_in(self):
        # This button might be on the employee's "My Dashboard" tab
        my_dashboard_tab = (By.XPATH, "//a[contains(@href, '#my_dashboard_for_employee')]")
        if self.is_element_visible(my_dashboard_tab):
             self.do_click(my_dashboard_tab) # Ensure the correct tab is active
        self.do_click(self.ONLINE_CHECK_IN_BUTTON)

    def get_check_in_button_text(self):
        # This requires finding the button that would toggle (check-in/check-out)
        # This is a simplification; actual state change might involve different elements.
        try:
            if self.is_element_visible(self.ONLINE_CHECK_IN_BUTTON):
                return self.get_element_text(self.ONLINE_CHECK_IN_BUTTON)
        except: # If check-in button not found, maybe check-out button is visible
            if self.is_element_visible(self.ONLINE_CHECK_OUT_BUTTON):
                 return self.get_element_text(self.ONLINE_CHECK_OUT_BUTTON)
        return "Button Not Found"
