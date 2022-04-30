import pytest

from Pages.Pages_2.rsa_home_page import RsaHomePage


@pytest.mark.usefixtures("setup")
class TestRsa:
    def test_tc01(self):
        self.driver.get("https://rahulshettyacademy.com/locatorspractice")
        home = RsaHomePage(self.driver)
        home.click_signin_button()
        expected_error_msg = "* Incorrect username or password"
        assert expected_error_msg == home.get_login_error_msg()

    def test_tc02(self):
        self.driver.refresh()
        home = RsaHomePage(self.driver)
        home.click_check_box1()
        home.click_check_box2()
        home.click_signin_button()
        expected_error_msg = "* Incorrect username or password"
        assert expected_error_msg == home.get_login_error_msg()

