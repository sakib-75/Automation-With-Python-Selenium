import time
from selenium.webdriver.common.by import By
from Utilities.common_method_1 import send_text


class RsaHomePage:
    def __init__(self, driver):
        self.driver = driver

    user_name = (By.ID, "inputUsername")
    password = (By.NAME, "inputPassword")
    check_box1 = (By.ID, "chkboxOne")
    check_box2 = (By.ID, "chkboxTwo")
    forgot_pass_link = (By.LINK_TEXT, "Forgot your password?")
    signin_btn = (By.XPATH, "//button[text()='Sign In']")
    error_msg = (By.CSS_SELECTOR, "p.error")

    # Forgot password part
    name_inp = (By.XPATH, "//input[@placeholder='Name']")
    email_inp = (By.XPATH, "//input[@placeholder='Email']")
    phone_inp = (By.XPATH, "//input[@placeholder='Phone Number']")
    reset_btn = (By.CLASS_NAME, "reset-pwd-btn")
    goto_login_btn = (By.CLASS_NAME, "go-to-login-btn")
    info_msg = (By.CSS_SELECTOR, "p.infoMsg")

    def login(self, username, password):
        username_inp = self.driver.find_element(*self.user_name)
        password_inp = self.driver.find_element(*self.password)
        send_text(username_inp, username)
        send_text(password_inp, password)
        self.click_check_box1()
        self.click_check_box2()
        self.click_signin_button()

    def click_check_box1(self):
        self.driver.find_element(*self.check_box1).click()

    def click_check_box2(self):
        self.driver.find_element(*self.check_box2).click()

    def click_signin_button(self):
        self.driver.find_element(*self.signin_btn).click()

    def get_login_error_msg(self):
        error_msg = self.driver.find_element(*self.error_msg).text
        return error_msg

    def click_forgot_password(self):
        self.driver.find_element(*self.forgot_pass_link).click()

    def reset_login(self, name, email, phone):
        name_inp = self.driver.find_element(*self.name_inp)
        email_inp = self.driver.find_element(*self.email_inp)
        phone_inp = self.driver.find_element(*self.phone_inp)
        send_text(name_inp, name)
        send_text(email_inp, email)
        send_text(phone_inp, phone)
        time.sleep(1)
        self.driver.find_element(*self.reset_btn).click()

    def get_password(self):
        text = self.driver.find_element(*self.info_msg).text
        pass_array = text.split("'")
        password = pass_array[1].split("'")[0]
        return password

    def click_goto_login_btn(self):
        self.driver.find_element(*self.goto_login_btn).click()
