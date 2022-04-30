from selenium.webdriver import ActionChains


def hover_element(driver, element):
    actions = ActionChains(driver)
    actions.click_and_hold(element).perform()
