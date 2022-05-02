import time
import pytest

from Pages.rsa_home_page import RsaHomePage


@pytest.mark.usefixtures("setup")
class TestRsaForgotPassword:
    def test_forgot_password(self):
        self.driver.get("https://rahulshettyacademy.com/locatorspractice")
        home = RsaHomePage(self.driver)
        home.click_forgot_password()
        home.reset_login("sakib", "sakib@gmail.com", "01923453212")
        password = home.get_password()
        home.click_goto_login_btn()
        self.driver.refresh()
        home.login("sakib", password)
        time.sleep(2)
