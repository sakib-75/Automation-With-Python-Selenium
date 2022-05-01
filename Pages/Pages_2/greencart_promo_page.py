from selenium.webdriver.common.by import By

from Utilities.common_method_1 import send_text


class GreenkartPromo:
    def __init__(self, driver):
        self.driver = driver

    promo_code_inp = (By.CLASS_NAME, "promoCode")
    promo_code_apply = (By.CLASS_NAME, "promoBtn")
    promo_info = (By.CSS_SELECTOR, "span.promoInfo")
    place_order_btn_path = (By.XPATH, "//button[text()='Place Order']")

    def enter_promo_code(self, promo_code):
        promo_code_inp = self.driver.find_element(*self.promo_code_inp)
        send_text(promo_code_inp, promo_code)

    def click_apply_promo(self):
        self.driver.find_element(*self.promo_code_apply).click()

    def get_promo_info(self):
        promo_info = self.driver.find_element(*self.promo_info).text
        return promo_info

    def click_place_order(self):
        self.driver.find_element(*self.place_order_btn_path).click()
