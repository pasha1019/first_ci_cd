import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)  # seconds between poll

    def open(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.driver.get(self.PAGE_URL)  # open page

    def is_opened(self):
        self.wait.until(ec.url_to_be(self.PAGE_URL))  # login page is opened

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
