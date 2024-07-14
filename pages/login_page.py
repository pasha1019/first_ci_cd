import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    USERNAME_FIELD = ("xpath", "//input[@name='username']")  # login
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")  # password
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")  # login button

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(ec.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)  # enter login

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(ec.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)  # enter pass

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON)).click()  # click login button
