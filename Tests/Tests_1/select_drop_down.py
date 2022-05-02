import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestSelectDropDown:
    def test_select_drop_down(self):
        driver = self.driver
        actions = self.actions
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
        driver.switch_to.frame("iframeResult")

        select_element = driver.find_element(By.NAME, "cars")
        select = Select(select_element)
        select.select_by_index(0)

        actions.key_down(Keys.CONTROL) \
            .click(select.options[3]) \
            .click(select.options[1]) \
            .key_up(Keys.CONTROL).perform()

        driver.switch_to.default_content()
        time.sleep(2)

        # select.select_by_visible_text("text")
        # select.select_by_value(value)
        # select.deselect_all()
        # select.deselect_by_index()
        # select.deselect_by_visible_text()
        # select.deselect_by_value()
        # select.all_selected_options
        # select.first_selected_option
        # select.options
