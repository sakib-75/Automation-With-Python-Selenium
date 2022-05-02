import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestClickAction:
    def test_click_action(self):
        driver = self.driver
        actions = self.actions
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
        driver.switch_to.frame("iframeResult")

        element_1 = driver.find_element(By.CSS_SELECTOR, "body > p:nth-child(2)")
        element_2 = driver.find_element(By.XPATH, "//body/form[1]/input[1]")

        actions.double_click(element_1).perform()
        time.sleep(2)
        actions.context_click(element_2).perform()
        time.sleep(2)
