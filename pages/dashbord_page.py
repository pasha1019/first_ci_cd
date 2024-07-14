import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class DashbordPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE
    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step("Click on to My Info")
    def click_my_info_link(self):
        self.wait.until(ec.element_to_be_clickable(self.MY_INFO_BUTTON)).click()  # my_info button click
