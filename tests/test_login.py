import pytest
from vyper import v as configuration

from pages.login_page import LoginPage


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.open_login_page()
    return page


class TestLogin:
    username = configuration.get('user').get('username')

    @pytest.mark.parametrize('username', [username, username.upper(), f' {username} '],
                             ids=['exact username', 'switched case', 'with white spaces'])
    def test_valid_credential(self, login_page, username, user_credential):
        login_page.fill_form(username=username, password=user_credential['password'])
        avatar = login_page.get_element(LoginPage._PROFILE_AVATAR)
        assert avatar.is_displayed()

    def test_invalid_password(self, login_page, user_credential):
        login_page.fill_form(username=user_credential['username'], password='wrong')
        error = login_page.get_element(login_page.PASSWORD_ERROR)
        assert error.text == 'Password or email is incorrect.'

    def test_invalid_username(self, login_page, user_credential):
        login_page.fill_form(username=user_credential['username'], password=user_credential['password'])
        error = login_page.get_element(login_page.USERNAME_ERROR)
        assert error.text == 'Password or email is incorrect.'

    def test_password_wrong_case(self, login_page, user_credential):
        login_page.fill_form(username=user_credential['username'], password=user_credential['password'].upper())
        error = login_page.get_element(login_page.PASSWORD_ERROR)
        assert error.text == 'Password or email is incorrect.'
