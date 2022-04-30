from selenium.webdriver.common.by import By


class RsaHomePage:
    def __init__(self, driver):
        self.driver = driver

        self.user_name_id = "inputUsername"
        self.password_id = "inputPassword"
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

    def click_check_box1(self):
        self.driver.find_element(By.ID, self.check_box1_id).click()

    def click_check_box2(self):
        self.driver.find_element(By.ID, self.checkbox2_id).click()

    def click_signin_button(self):
        self.driver.find_element(By.XPATH, self.signin_btn_xpath).click()

    def get_login_error_msg(self):
        error_msg = self.driver.find_element(By.CSS_SELECTOR, self.error_msg_css).text
        return error_msg
