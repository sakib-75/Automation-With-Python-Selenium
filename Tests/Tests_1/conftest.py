import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    actions = ActionChains(driver)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.actions = actions
    yield
    driver.quit()
