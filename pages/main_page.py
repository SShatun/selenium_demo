import allure
from selenium.webdriver.common.by import By
from vyper import v as configuration

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = configuration.get('host')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-link-dark btn-login']")
    PROFILE_AVATAR = (By.CSS_SELECTOR, ".profile-nav-avatar")

    @allure.step("Open login page")
    def open_login_page(self):
        self.navigate_to(self.URL)
        self.get_element(self.LOGIN_BUTTON).click()
