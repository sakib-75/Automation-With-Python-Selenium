from selenium.webdriver.common.by import By

from Utilities.common_method_1 import send_text


class GreenkartPromo:
    def __init__(self, driver):
        self.driver = driver

    promo_code_inp_class = "promoCode"
    promo_code_apply_class = "promoBtn"
    promo_info_css = "span.promoInfo"
    place_order_btn_xpath = "//button[text()='Place Order']"

    def enter_promo_code(self, promo_code):
        promo_code_inp = self.driver.find_element(By.CLASS_NAME, self.promo_code_inp_class)
        send_text(promo_code_inp, promo_code)

    def click_apply_promo(self):
        self.driver.find_element(By.CLASS_NAME, self.promo_code_apply_class).click()

    def get_promo_info(self):
        promo_info = self.driver.find_element(By.CSS_SELECTOR, self.promo_info_css).text
        return promo_info
