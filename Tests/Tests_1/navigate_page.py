import pytest


@pytest.mark.usefixtures("setup")
class TestNavigatePage:
    def test_navigate_page(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.back()
        driver.forward()
        driver.refresh()
