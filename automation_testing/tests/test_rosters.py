# tests/test_rosters.py
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.roster_page import RosterPage # Create this page object
from pages.settings_page import SettingsPage # For WorkSlot CRUD
from utils.config import ADMIN_USERNAME, ADMIN_PASSWORD

@pytest.mark.rosters
class TestRosters:

    @pytest.fixture(autouse=True)
    def login_once(self, driver):
        login_pg = LoginPage(driver)
        assert login_pg.login(ADMIN_USERNAME, ADMIN_PASSWORD), "Login failed"
        self.dashboard_pg = DashboardPage(driver)
        assert self.dashboard_pg.is_dashboard_visible(), "Dashboard not visible after login"


    def test_tc_ros_001_navigate_to_employee_roster(self, driver):
        """TC_ROS_001: Verify navigating to Employee Roster page"""
        # dashboard_pg = DashboardPage(driver) # Using self.dashboard_pg
        self.dashboard_pg.navigate_to_employee_roster()
        roster_pg = RosterPage(driver) # Assuming RosterPage has a method to verify its visibility
        assert roster_pg.is_employee_roster_page_visible(), "Employee Roster page not loaded"

    def test_tc_ros_011_create_work_slot_valid(self, driver):
        """TC_ROS_011: Verify Work Slot CRUD - Create new Work Slot with valid data"""
        # dashboard_pg = DashboardPage(driver) # Using self.dashboard_pg
        self.dashboard_pg.navigate_to_workslot_settings()
        
        settings_pg = SettingsPage(driver) # SettingsPage will handle WorkSlot interactions
        settings_pg.click_add_new_workslot() # Method in SettingsPage
        
        title = "Morning Shift PyTest"
        start_time = "09:00" # Format might be HH:mm AM/PM or 24hr
        end_time = "17:00"
        late_time = "09:05"
        
        settings_pg.enter_workslot_details(title, start_time, end_time, late_time)
        settings_pg.click_save_workslot()
        
        success_msg = settings_pg.get_general_success_message() # A generic success message getter
        assert success_msg and "success" in success_msg.lower(), "Failed to create WorkSlot or success message not shown."
        assert settings_pg.is_workslot_in_list(title), f"WorkSlot '{title}' not found in list."

    # ... Add more test cases for Rosters (TC_ROS_002 to TC_ROS_030) ...
