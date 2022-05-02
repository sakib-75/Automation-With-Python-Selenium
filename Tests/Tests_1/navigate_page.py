import pytest
from Utilities.screenshot import screenshot_for_allure


@pytest.mark.usefixtures("setup")
class TestNavigatePage:
    def test_navigate_page(self):
        driver = self.driver
        driver.get("http://www.google.com")
        screenshot_for_allure(driver, "Test screenshot")
        driver.back()
        driver.forward()
        driver.refresh()
