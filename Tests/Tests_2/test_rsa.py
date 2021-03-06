import pytest

from Pages.rsa_home_page import RsaHomePage


@pytest.mark.usefixtures("setup")
class TestRsa:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://rahulshettyacademy.com/locatorspractice")
        self.expected_error_msg = "* Incorrect username or password"
        self.home = RsaHomePage(self.driver)
        yield
        assert self.expected_error_msg == self.home.get_login_error_msg()

    def test_all_empty_input(self):
        self.home.click_signin_button()

    def test_empty_input(self):
        self.home.click_check_box1()
        self.home.click_check_box2()
        self.home.click_signin_button()

    def test_signup_wrong(self):
        self.driver.refresh()
        self.home.login("sakib", "123")
