import time
from selenium.webdriver.common.by import By
from Utilities.common_method_1 import send_text


class RsaHomePage:
    def __init__(self, driver):
        self.driver = driver

    user_name_id = "inputUsername"
    password_name = "inputPassword"
    check_box1_id = "chkboxOne"
    checkbox2_id = "chkboxTwo"
    forgot_pass_link = "Forgot your password?"
    signin_btn_xpath = "//button[text()='Sign In']"
    error_msg_css = "p.error"

    # Forgot password part
    name_inp_xpath = "//input[@placeholder='Name']"
    email_inp_xpath = "//input[@placeholder='Email']"
    phone_inp_xpath = "//input[@placeholder='Phone Number']"
    reset_btn_class = "reset-pwd-btn"
    goto_login_btn_class = "go-to-login-btn"
    info_msg_css = "p.infoMsg"

    def login(self, username, password):
        username_inp = self.driver.find_element(By.ID, self.user_name_id)
        password_inp = self.driver.find_element(By.NAME, self.password_name)
        send_text(username_inp, username)
        send_text(password_inp, password)
        self.click_check_box1()
        self.click_check_box2()
        self.click_signin_button()

    def click_check_box1(self):
        self.driver.find_element(By.ID, self.check_box1_id).click()

    def click_check_box2(self):
        self.driver.find_element(By.ID, self.checkbox2_id).click()

    def click_signin_button(self):
        self.driver.find_element(By.XPATH, self.signin_btn_xpath).click()

    def get_login_error_msg(self):
        error_msg = self.driver.find_element(By.CSS_SELECTOR, self.error_msg_css).text
        return error_msg

    def click_forgot_password(self):
        self.driver.find_element(By.LINK_TEXT, self.forgot_pass_link).click()

    def reset_login(self, name, email, phone):
        name_inp = self.driver.find_element(By.XPATH, self.name_inp_xpath)
        email_inp = self.driver.find_element(By.XPATH, self.email_inp_xpath)
        phone_inp = self.driver.find_element(By.XPATH, self.phone_inp_xpath)
        send_text(name_inp, name)
        send_text(email_inp, email)
        send_text(phone_inp, phone)
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, self.reset_btn_class).click()

    def get_password(self):
        text = self.driver.find_element(By.CSS_SELECTOR, self.info_msg_css).text
        pass_array = text.split("'")
        password = pass_array[1].split("'")[0]
        return password

    def click_goto_login_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.goto_login_btn_class).click()
