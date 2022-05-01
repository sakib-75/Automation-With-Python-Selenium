import time
import pytest

from Pages.Pages_2.greencart_promo_page import GreenkartPromo
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
        assert len(produc_name_list) == home.get_cart_items()
        time.sleep(2)

    def test_apply_promo(self):
        promo = GreenkartPromo(self.driver)
        promo.enter_promo_code("rahulshettyacademy")
        promo.click_apply_promo()
        assert promo.get_promo_info() == "Code applied ..!"
        promo.click_place_order()
