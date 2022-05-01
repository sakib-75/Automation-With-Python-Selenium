import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestAlertPopupWindow:
    def test_alert_handling(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

        frame = driver.find_element(By.NAME, "iframeResult")
        driver.switch_to.frame(frame)

        driver.find_element(By.XPATH, "//button[text()='Try it']").click()
        time.sleep(2)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()

        driver.switch_to.default_content()

        # alert_obj.accept() – used to accept the Alert
        # alert_obj.dismiss() – used to cancel the Alert
        # alert_obj.send_keys() – used to enter a value in the Alert text box
        # alert_obj.text() – used to retrieve the message included in the Alert pop-up
