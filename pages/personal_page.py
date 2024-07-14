import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")  # first name field
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")  # save button
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        with (allure.step(f"Change name on '{new_name}'")):
            first_name_field = self.wait.until(ec.element_to_be_clickable(self.FIRST_NAME_FIELD))  # get firstname
            first_name_field.send_keys(Keys.CONTROL + "A")  # command for ios
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)  # enter new name
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(ec.element_to_be_clickable(self.SAVE_BUTTON)).click()  # click save button

    @allure.step("Changes has been successfully")
    def is_changes_saved(self):
        self.wait.until(ec.invisibility_of_element_located(self.SPINNER))
        self.wait.until(ec.visibility_of_element_located(self.FIRST_NAME_FIELD))  # check name field
        self.wait.until(ec.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))  # check changes saved
