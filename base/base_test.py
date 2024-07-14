import pytest
from pages.login_page import LoginPage
from pages.dashbord_page import DashbordPage
from pages.personal_page import PersonalPage
from config.data import Data


class BaseTest:
    login_page: LoginPage
    dashbord_page: DashbordPage
    personal_page: PersonalPage
    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashbord_page = DashbordPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.data = Data()
