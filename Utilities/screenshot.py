from datetime import datetime

import allure
from allure_commons.types import AttachmentType


def take_screenshot(driver, name):
    full_time = current_date_time()
    folder_path = "C:\\Users\\LENOVO\\PycharmProjects\\Automation-With-Python-Selenium\\images\\"
    driver.save_screenshot(folder_path + name + "_" + full_time + ".png")


def current_date_time():
    date_time = datetime.now()
    date = str(date_time.date())
    hour = str(date_time.hour)
    minute = str(date_time.minute)
    second = str(date_time.second)
    full_date_time = (date + "_" + hour + "h-" + minute + "m-" + second + "s")
    return full_date_time


def screenshot_for_allure(driver, file_name):
    allure.attach(driver.get_screenshot_as_png(),
                  name=file_name,
                  attachment_type=AttachmentType.PNG)
