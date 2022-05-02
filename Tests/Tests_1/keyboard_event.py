import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Utilities.common_method_1 import hover_element


@pytest.mark.usefixtures("setup")
class TestKeyboardEvent:
    def test_keyboard_event(self):
        driver = self.driver
        actions = self.actions
        driver.get("http://automationpractice.com/index.php")

        search_input = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
        dresses_button = driver.find_element(By.XPATH, "(//a[@title='Dresses'])[2]")
        casual_dresses_button = driver.find_element(By.XPATH, "(//a[@title='Casual Dresses'])[2]")

        actions.move_to_element(search_input).click()\
            .key_down(Keys.SHIFT)\
            .send_keys("tech")\
            .send_keys(Keys.ENTER).perform()

        hover_element(driver, dresses_button)
        casual_dresses_button.click()



