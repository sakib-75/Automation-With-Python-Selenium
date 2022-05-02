import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestWindowHandling:
    def test_window_handling(self):
        driver = self.driver
        driver.get("https://sakibul-islam.netlify.app")

        driver.find_element(By.XPATH, "//section[@id='about']//div[3]//a[1]").click()
        driver.find_element(By.XPATH, "//section[@id='about']//div[4]//a[1]").click()
        print(driver.title)
        time.sleep(2)

        all_tabs = driver.window_handles

        driver.switch_to.window(all_tabs[1])
        print(driver.title)
        time.sleep(2)

        driver.switch_to.window(all_tabs[0])
        print(driver.title)
        time.sleep(2)
