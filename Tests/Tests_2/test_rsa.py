import pytest

from Pages.Pages_2.rsa_home_page import RsaHomePage


@pytest.mark.usefixtures("setup")
class TestRsa:
    expected_error_msg = "* Incorrect username or password"

    def test_all_empty_input(self):
        self.driver.get("https://rahulshettyacademy.com/locatorspractice")
        home = RsaHomePage(self.driver)
        home.click_signin_button()
        assert self.expected_error_msg == home.get_login_error_msg()

    def test_empty_input(self):
        self.driver.refresh()
        home = RsaHomePage(self.driver)
        home.click_check_box1()
        home.click_check_box2()
        home.click_signin_button()
        assert self.expected_error_msg == home.get_login_error_msg()

    def test_signup_wrong(self):
        self.driver.refresh()
        home = RsaHomePage(self.driver)
        home.login("sakib", "123")
        assert self.expected_error_msg == home.get_login_error_msg()
