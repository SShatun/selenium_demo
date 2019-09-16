import pytest
from vyper import v as configuration

from pages.login_page import LoginPage
from utils import wait_for


class TestLogin:
    username = configuration.get('user').get('username')
    password = configuration.get('user').get('password')

    @pytest.fixture()
    def login_page(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        return page

    @pytest.fixture()
    def login_captcha(self, login_page):
        login_page.fill_form('wrong', 'wrong')
        login_page.submit()
        login_page.submit()
        assert login_page.get_element(login_page.CAPTCHA_FIELD).is_displayed()
        return login_page

    @pytest.mark.parametrize('username', [username, username.upper(), f' {username} '],
                             ids=['exact username', 'switched case', 'with white spaces'])
    def test_valid_credential(self, login_page, username):
        login_page.fill_form(username=username, password=self.password)
        avatar = login_page.get_element(LoginPage.PROFILE_AVATAR)
        assert avatar.is_displayed()

    @pytest.mark.parametrize('password', ['wrong', password.upper(), f' {password} '],
                             ids=['invalid', 'switched case', 'with white spaces'])
    def test_invalid_password(self, password, login_page):
        login_page.fill_form(username=self.username, password=password)
        error = login_page.get_element(login_page.PASSWORD_ERROR)
        assert error.text == 'Password or email is incorrect.'

    @pytest.mark.parametrize('password', [password, ''], ids=['password filled', 'password empty'])
    @pytest.mark.parametrize('username', [username, ''], ids=['username filled', 'username empty'])
    def test_empty_fields(self, login_page, password, username):
        login_page.fill_form(username=username, password=password)
        if not username:
            assert login_page.get_element(login_page.USERNAME_ERROR).is_displayed()
        if not password:
            assert login_page.get_element(login_page.PASSWORD_ERROR).is_displayed()

    def test_invalid_username(self, login_page, user_credential):
        login_page.fill_form(username='wrong', password=self.password)
        error = login_page.get_element(login_page.USERNAME_ERROR)
        assert error.text == 'Password or email is incorrect.'

    def test_refresh_captcha(self, login_captcha):
        img_before = login_captcha.get_element(login_captcha.CAPTCHA_IMG).get_attribute("src")
        login_captcha.refresh_captcha()
        wait_for(login_captcha.get_element(login_captcha.CAPTCHA_IMG).get_attribute("src") != img_before)
        assert login_captcha.get_element(login_captcha.CAPTCHA_IMG).get_attribute("src") != img_before

    def test_wrong_captcha(self, login_captcha):
        login_captcha.enter_captcha('value')
        assert login_captcha.get_element(login_captcha.CAPTCHA_ERROR).is_displayed()

    @pytest.mark.parametrize('social, tittle',
                             [(LoginPage.FACEBOOK_BUTTON, 'Facebook'),
                              (LoginPage.GOOGLE_BUTTON, 'Google')],
                             ids=['Facebook', 'Google'])
    def test_social_auth(self, login_page, social, tittle):
        login_page.get_element(social).click()
        wait_for(len(login_page._driver.window_handles) > 1)
        login_page._driver.switch_to.window(login_page._driver.window_handles[1])
        assert tittle in login_page._driver.title
