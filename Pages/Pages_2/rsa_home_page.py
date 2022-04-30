from selenium.webdriver.common.by import By

from Utilities.common_method_1 import send_text


class RsaHomePage:
    def __init__(self, driver):
        self.driver = driver

        self.user_name_id = "inputUsername"
        self.password_name = "inputPassword"
        self.check_box1_id = "chkboxOne"
        self.checkbox2_id = "chkboxTwo"
        self.forgot_pass_link = "Forgot your password?"
        self.signin_btn_xpath = "//button[text()='Sign In']"
        self.error_msg_css = "p.error"

        # Forgot password part
        self.name_inp_xpath = "//input[@placeholder='Name']"
        self.email_inp_xpath = "//input[@placeholder='Email']"
        self.phone_inp_xpath = "//input[@placeholder='Phone Number']"
        self.reset_btn_class = "reset-pwd-btn"
        self.goto_login_btn_class = "go-to-login-btn"
        self.info_msg_css = "p.infoMsg"

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
