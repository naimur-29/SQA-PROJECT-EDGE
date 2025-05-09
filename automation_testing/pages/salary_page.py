# AmaderHR_Automation/pages/salary_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SalaryPage(BasePage):
    # --- Locators for Salary & Pay Grade Management ---
    # Example (replace with actual locators)
    PAY_GRADES_PAGE_HEADER = (By.XPATH, "//h3[contains(text(),'Grades')]") # Or a more unique element for the grades list page
    ADD_NEW_GRADE_BUTTON = (By.XPATH, "//a[contains(text(),'Add New Grade') or contains(@class,'btn-primary') and .//i[contains(@class,'fa-plus')]]") # Placeholder
    GRADE_NAME_INPUT = (By.ID, "grade_name") # Placeholder - check actual ID/name
    GRADE_RANGE_START_INPUT = (By.ID, "range_start") # Placeholder
    GRADE_RANGE_END_INPUT = (By.ID, "range_end") # Placeholder
    SAVE_GRADE_BUTTON = (By.XPATH, "//button[@type='submit' and (contains(text(),'Save') or contains(text(),'Create'))]") # Placeholder
    PAY_GRADE_TABLE = (By.ID, "payGradeTable") # Placeholder for the table listing pay grades
    
    EARNINGS_PAGE_HEADER = (By.XPATH, "//h3[contains(text(),'Earning')]")
    ADD_NEW_EARNING_BUTTON = (By.XPATH, "//a[contains(text(),'Add New Earning')]") # Placeholder
    EARNING_TITLE_INPUT = (By.ID, "earning_title") # Placeholder
    # ... other earning fields
    SAVE_EARNING_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(),'Save Earning')]") # Placeholder

    DEDUCTIONS_PAGE_HEADER = (By.XPATH, "//h3[contains(text(),'Deduction')]")
    # ... similar locators for Deductions

    PREPARE_SALARY_HEADER = (By.XPATH, "//h3[contains(text(),'Prepare Salary')]")
    # ... locators for prepare salary filters (month, year, employee dropdowns) and buttons

    SALARY_LIST_HEADER = (By.XPATH, "//h3[contains(text(),'Salary List')]")
    # ... locators for salary list table, filters, view payslip buttons

    BONUS_SETTINGS_HEADER = (By.XPATH, "//h3[contains(text(),'Bonus Settings')]")
    # ...
    GENERATE_BONUS_HEADER = (By.XPATH, "//h3[contains(text(),'Generate Bonus')]")
    # ...

    SUCCESS_MESSAGE_GENERIC = (By.XPATH, "//div[contains(@class, 'alert-success') or contains(@class,'swal2-success-ring')]")


    def __init__(self, driver):
        super().__init__(driver)

    def is_pay_grades_page_visible(self):
        return self.is_element_visible(self.PAY_GRADES_PAGE_HEADER)

    def click_add_new_pay_grade(self):
        self.do_click(self.ADD_NEW_GRADE_BUTTON)

    def enter_pay_grade_details(self, name, range_start, range_end):
        self.do_send_keys(self.GRADE_NAME_INPUT, name)
        self.do_send_keys(self.GRADE_RANGE_START_INPUT, range_start)
        self.do_send_keys(self.GRADE_RANGE_END_INPUT, range_end)
        # Add other fields if necessary

    def click_save_pay_grade(self):
        self.do_click(self.SAVE_GRADE_BUTTON)

    def get_general_success_message(self):
        if self.is_element_visible(self.SUCCESS_MESSAGE_GENERIC):
            return self.get_element_text(self.SUCCESS_MESSAGE_GENERIC)
        return None

    def is_pay_grade_in_list(self, grade_name):
        # This will need actual table traversal or a specific XPath
        # For now, a placeholder check
        if not self.is_element_visible(self.PAY_GRADE_TABLE): # Assuming you have a PAY_GRADE_TABLE locator
            return False
        try:
            # Example: Find a cell containing the grade_name text within the table
            grade_cell = self.find_element((By.XPATH, f"//table[@id='{self.PAY_GRADE_TABLE[1]}']//td[contains(text(), '{grade_name}')]"))
            return grade_cell.is_displayed()
        except:
            return False

    # Add methods for:
    # - is_earnings_page_visible()
    # - click_add_new_earning()
    # - enter_earning_details()
    # - click_save_earning()
    # - is_earning_in_list()
    # - and similarly for Deductions, Prepare Salary, Salary List, Bonus, etc.
