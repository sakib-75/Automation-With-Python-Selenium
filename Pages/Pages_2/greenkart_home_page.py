from selenium.webdriver.common.by import By


class Greenkart:
    def __init__(self, driver):
        self.driver = driver

    all_product_title_css = "h4.product-name"
    all_add_to_cart_xpath = "//div[@class='product-action']"
    cart_icon_xpath = "//a[@class='cart-icon']"
    check_out_xpath = "//button[text()='PROCEED TO CHECKOUT']"
    cart_items_xpath = "(//td)[3]"

    def all_product_title(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.all_product_title_css)
        return elements

    def all_add_to_cart(self):
        elements = self.driver.find_elements(By.XPATH, self.all_add_to_cart_xpath)
        return elements

    def add_to_cart(self, product_list):
        count = 0
        products = self.all_product_title()
        for i in range(0, len(products), 1):
            product_title = products[i].text.split("-")
            product_name = product_title[0].strip()
            if product_list.count(product_name) > 0:
                self.all_add_to_cart()[i].click()
                count += 1
        print("Total added item in cart: ", count)

    def get_cart_items(self):
        cart_items = self.driver.find_element(By.XPATH, self.cart_items_xpath)
        return int(cart_items.text)

    def click_cart_icon(self):
        self.driver.find_element(By.XPATH, self.cart_icon_xpath).click()

    def click_check_out(self):
        self.driver.find_element(By.XPATH, self.check_out_xpath).click()
