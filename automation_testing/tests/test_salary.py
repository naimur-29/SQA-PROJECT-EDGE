# tests/test_salary.py
import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.salary_page import SalaryPage  # Create this page object
from pages.settings_page import SettingsPage  # For PayGrade etc.
from utils.config import ADMIN_PASSWORD, ADMIN_USERNAME


@pytest.mark.salary
class TestSalary:

    @pytest.fixture(autouse=True)
    def login_once(self, driver):
        login_pg = LoginPage(driver)
        assert login_pg.login(ADMIN_USERNAME, ADMIN_PASSWORD), "Login failed"
        self.dashboard_pg = DashboardPage(driver)
        assert self.dashboard_pg.is_dashboard_visible(), "Dashboard not visible after login"

    def test_tc_sal_001_navigate_to_pay_grades(self, driver):
        """TC_SAL_001: Verify navigation to Pay Grade Management - Grades"""
        # dashboard_pg = DashboardPage(driver) # Using self.dashboard_pg
        self.dashboard_pg.navigate_to_pay_grades()
        salary_pg = SalaryPage(driver) # Assuming SalaryPage has methods for PayGrade section
        assert salary_pg.is_pay_grades_page_visible(), "Pay Grades page not loaded"

    def test_tc_sal_002_create_pay_grade_valid(self, driver):
        """TC_SAL_002: Verify creating a new Pay Grade with valid data"""
        # dashboard_pg = DashboardPage(driver) # Using self.dashboard_pg
        self.dashboard_pg.navigate_to_pay_grades()
        
        salary_pg = SalaryPage(driver)
        salary_pg.click_add_new_pay_grade() # Method in SalaryPage
        
        grade_name = "Test Grade Py"
        range_start = "30000"
        range_end = "50000"
        
        salary_pg.enter_pay_grade_details(grade_name, range_start, range_end)
        salary_pg.click_save_pay_grade()
        
        success_msg = salary_pg.get_general_success_message()
        assert success_msg and "success" in success_msg.lower(), "Failed to create Pay Grade."
        assert salary_pg.is_pay_grade_in_list(grade_name), f"Pay Grade '{grade_name}' not found."

    # ... Add more test cases for Salary (TC_SAL_003 to TC_SAL_040) ...
