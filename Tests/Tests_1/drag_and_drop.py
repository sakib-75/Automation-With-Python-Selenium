import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestDragAndDrop:
    def test_drag_and_drop(self):
        driver = self.driver
        actions = self.actions
        driver.get("https://jqueryui.com/droppable")
        driver.switch_to.frame(0)

        drag_able = driver.find_element(By.ID, "draggable")
        drop_able = driver.find_element(By.ID, "droppable")

        actions.drag_and_drop(drag_able, drop_able).perform()

        driver.switch_to.default_content()
        time.sleep(2)
