import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestScrollPage:

    def test_scroll_page(self):
        driver = self.driver
        driver.get("https://www.seleniumhq.org")

        # scroll to pixel
        driver.execute_script("window.scrollTo(0,1000)", "")
        time.sleep(2)

        # scroll to bottom
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

        # scroll to top
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(2)

        # scroll to element
        element = driver.find_element(By.XPATH, "(//div[@class='row justify-content-center p-5'])[1]")
        driver.execute_script("arguments[0].scrollIntoView()", element)
        time.sleep(2)
