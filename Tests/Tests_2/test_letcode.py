import unittest
import pytest
from ddt import ddt, file_data
from Pages.Pages_2.letcode_pages import LetcodePages


@ddt
@pytest.mark.usefixtures("setup")
class TestLetcode(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://letcode.in/")
        self.lc = LetcodePages(self.driver)

    @file_data('../../Test_Data/user_dataset.json')
    def test_1signup(self, name, email, password):
        self.lc.click_signup()
        self.lc.signup(name, email, password)

    @file_data('../../Test_Data/user_dataset.json')
    def test_2login(self, name, email, password):
        self.lc.click_login()
        self.lc.login(email, password)
