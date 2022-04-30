import time
import pytest

from Pages.Pages_2.greenkart_home_page import Greenkart


@pytest.mark.usefixtures("setup")
class TestGreenkart:
    def test_add_to_cart(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise")
        produc_name_list = ["Carrot", "Brocolli", "Cucumber", "Potato"]
        home = Greenkart(self.driver)
        home.add_to_cart(produc_name_list)
        home.click_cart_icon()
        home.click_check_out()
        time.sleep(2)
