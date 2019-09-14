import allure
from selenium.webdriver.common.by import By

from pages.main_page import MainPage


class LoginPage(MainPage):
    USERNAME_FIELD = (By.ID, "UserLogin_username")
    PASSWORD_FIELD = (By.ID, "UserLogin_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    USERNAME_ERROR = (By.CSS_SELECTOR, "#login-form > div:nth-child(4) > small")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#login-form > div:nth-child(5) > small")
    CAPTCHA_ERROR = (By.CSS_SELECTOR, "#login-form > div:nth-child(6) > div > small")
    CAPTCHA_FIELD = (By.ID, "UserLogin_verifyCode")
    CAPTCHA_IMG = (By.ID, "yw0")
    CAPTCHA_BUTTON = (By.ID, "yw0_button")
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, ".btn-facebook")
    GOOGLE_BUTTON = (By.CSS_SELECTOR, ".btn-google")

    @allure.step("input username {username}")
    def input_username(self, username: str):
        self.get_element(self.USERNAME_FIELD).send_keys(username)

    @allure.step("input password {password}")
    def input_password(self, password: str):
        self.get_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("push submit button")
    def submit(self):
        self.get_element(self.SUBMIT_BUTTON).click()

    def fill_form(self, username: str, password: str):
        self.input_username(username)
        self.input_password(password)
        self.submit()

    @allure.step("push refresh captcha button")
    def refresh_captcha(self):
        self.get_element(self.CAPTCHA_BUTTON).click()

    @allure.step("input {value} for captcha")
    def enter_captcha(self, value: str):
        self.get_element(self.CAPTCHA_FIELD).send_keys(value)
        self.submit()
