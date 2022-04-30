from selenium.webdriver import ActionChains


def send_text(element, value):
    element.clear()
    element.send_keys(value)


def hover_element(driver, element):
    actions = ActionChains(driver)
    actions.click_and_hold(element).perform()
