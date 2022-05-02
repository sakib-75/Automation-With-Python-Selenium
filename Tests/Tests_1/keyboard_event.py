import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestKeyboardEvent:

    def test_keyboard_event(self):
        driver = self.driver
        actions = self.actions
        driver.get("http://automationpractice.com/index.php")

        search_input_path = (By.XPATH, "//input[@id='search_query_top']")
        dresses_button_path = (By.XPATH, "(//a[@title='Dresses'])[2]")
        casual_dresses_button = driver.find_element(By.XPATH, "(//a[@title='Casual Dresses'])[2]")

        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.element_to_be_clickable(search_input_path))
        dresses_button = wait.until(EC.visibility_of_element_located(dresses_button_path))

        actions.move_to_element(search_input).click() \
            .key_down(Keys.SHIFT) \
            .send_keys("tech") \
            .send_keys(Keys.ENTER).perform()

        actions.move_to_element(dresses_button) \
            .move_to_element(casual_dresses_button) \
            .click().perform()

    def test_2(self):
        driver = self.driver
        actions = self.actions
        driver.get("https://opensource-demo.orangehrmlive.com/")

        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").click()

        admin_menu = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        job_menu = driver.find_element(By.ID, "menu_admin_Job")
        employment_status_menu = driver.find_element(By.ID, "menu_admin_employmentStatus")

        actions.move_to_element(admin_menu) \
            .move_to_element(job_menu) \
            .move_to_element(employment_status_menu) \
            .click().perform()
        time.sleep(3)
