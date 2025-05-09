# tests/test_attendance.py
import pytest
from pages.attendance_page import AttendancePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.config import (ADMIN_PASSWORD,  # Make sure these are correctly set
                          ADMIN_USERNAME)


@pytest.mark.attendance
class TestAttendance:

    @pytest.fixture(autouse=True)
    def login_once(self, driver):
        login_pg = LoginPage(driver)
        assert login_pg.login(ADMIN_USERNAME, ADMIN_PASSWORD), "Login failed"
        self.dashboard_pg = DashboardPage(driver) # Make dashboard_pg available to test methods
        assert self.dashboard_pg.is_dashboard_visible(), "Dashboard not visible after login"


    def test_tc_att_001_online_check_in(self, driver):
        """TC_ATT_001: Verify successful online check-in"""
        # Assuming user is not checked in initially (may need a pre-condition to ensure this)
        # dashboard_pg = DashboardPage(driver) # Now using self.dashboard_pg
        initial_button_text = self.dashboard_pg.get_check_in_button_text()
        if "Check Out" in initial_button_text:
            pytest.skip("User already checked in or check-out button present. Skipping check-in test.")
            # Or implement a check-out first if that's the desired flow
        
        self.dashboard_pg.click_online_check_in()
        # Add assertion for success message if one appears
        # For example:
        # success_popup = (By.XPATH, "//div[contains(@class, 'swal2-success')]") 
        # assert self.dashboard_pg.is_element_visible(success_popup), "Success message not shown for check-in"
        
        # Verify button text changes (this is a common pattern, actual implementation might vary)
        # Allowing some time for the page to update
        driver.implicitly_wait(2) # Temporary wait for demo, better to use explicit waits for specific elements
        updated_button_text = self.dashboard_pg.get_check_in_button_text()
        assert "Check Out" in updated_button_text, f"Button text did not change to 'Check Out'. Found: {updated_button_text}"
        # Further verification: Check attendance log on dashboard or in a report

    def test_tc_att_005_view_online_attendance_list(self, driver):
        """TC_ATT_005: Verify viewing 'Online Attendance' list for admin"""
        # dashboard_pg = DashboardPage(driver) # Now using self.dashboard_pg
        self.dashboard_pg.navigate_to_online_attendance()
        attendance_pg = AttendancePage(driver)
        assert attendance_pg.is_online_attendance_table_visible(), "Online attendance table not visible"
        # Add assertions to check for table headers or some data if possible

    def test_tc_att_013_add_new_device_valid(self, driver):
        """TC_ATT_013: Verify 'Devices' page - Add new device with valid data"""
        # dashboard_pg = DashboardPage(driver) # Now using self.dashboard_pg
        self.dashboard_pg.navigate_to_devices()
        
        attendance_pg = AttendancePage(driver)
        attendance_pg.click_add_new_device()
        
        device_name = "TestDevicePyTest"
        device_ip = "192.168.1.150"
        device_port = "4370"
        
        attendance_pg.enter_device_details(device_name, device_ip, device_port)
        attendance_pg.click_save_device()
        
        success_msg = attendance_pg.get_success_message()
        assert success_msg is not None and "successfully" in success_msg.lower(), f"Success message not found or incorrect. Msg: {success_msg}"
        assert attendance_pg.is_device_in_table(device_name), f"Device '{device_name}' not found in table after adding."

    # --- Placeholder for other Attendance Test Cases ---
    # You would continue adding test methods here, following the pattern:
    # 1. Navigate using DashboardPage methods.
    # 2. Interact with elements using AttendancePage (or other relevant page) methods.
    # 3. Assert expected outcomes.

    # Example of a test that might fail (for screenshot demo)
    @pytest.mark.xfail # You can mark tests expected to fail
    def test_tc_att_000_intentional_fail_for_screenshot(self, driver):
        """An intentionally failing test to demonstrate screenshots."""
        # dashboard_pg = DashboardPage(driver) # Now using self.dashboard_pg
        self.dashboard_pg.navigate_to_daily_attendance()
        assert False, "This test is designed to fail for screenshot demonstration."

    # ... Add more test cases for Attendance (TC_ATT_002 to TC_ATT_030) ...
    # For TC_ATT_002 (Check-out), you might need to ensure check-in happened first.
    # This can be done by ordering tests (less ideal with pytest) or by
    # making test_tc_att_002 perform a check-in if not already checked in.
    # A better way is to have setup fixtures or helper methods within the test class.

    # Example for TC_ATT_002
    def test_tc_att_002_online_check_out(self, driver):
        """TC_ATT_002: Verify successful online check-out"""
        # dashboard_pg = DashboardPage(driver) # Now using self.dashboard_pg
        current_button_text = self.dashboard_pg.get_check_in_button_text()
        
        if "Check In" in current_button_text:
            # If not checked in, perform check-in first for this test to proceed
            self.dashboard_pg.click_online_check_in()
            driver.implicitly_wait(2) # Allow time for UI update
            # Add assertion for successful check-in if necessary
            assert "Check Out" in self.dashboard_pg.get_check_in_button_text(), "Pre-condition: Check-in failed for check-out test"
        
        # Now proceed with check-out
        # This locator needs to be specific to the check-out button
        check_out_button = (By.XPATH, "//button[contains(text(), 'Online Check Out')]") 
        self.dashboard_pg.do_click(check_out_button)
        
        driver.implicitly_wait(2)
        updated_button_text = self.dashboard_pg.get_check_in_button_text()
        assert "Check In" in updated_button_text, f"Button text did not change to 'Check In' after checkout. Found: {updated_button_text}"
