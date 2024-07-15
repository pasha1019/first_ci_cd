import random
import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):
    @allure.title("Change profile name")
    @allure.severity("CRITICAL")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()  # open login page
        self.login_page.enter_login(self.data.LOGIN)  # login
        self.login_page.enter_password(self.data.PASSWORD)    # password
        self.login_page.click_submit_button()  # click button
        self.dashbord_page.is_opened()  # page opened
        self.dashbord_page.click_my_info_link()  # go to my info page
        self.personal_page.is_opened()  # page opened
        self.personal_page.change_name(f"Test {random.randint(1, 100)}")  # change name
        self.personal_page.save_changes()  # save changes
        self.personal_page.is_changes_saved()  # changes saved
        self.personal_page.make_screenshot("Success")
