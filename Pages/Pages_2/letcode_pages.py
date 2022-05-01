from selenium.webdriver.common.by import By
from Utilities.common_method_1 import send_text


class LetcodePages:
    def __init__(self, driver):
        self.driver = driver

    # home page
    signup_xpath = "//a[normalize-space()='Sign up']"
    login_xpath = "//a[normalize-space()='Log in']"
    logo_xpath = "//a[@class='navbar-item']"

    # signup page
    name_inp_id = "name"
    email_inp_id = "email"
    password_inp_id = "pass"
    tc_agree_id = "agree"
    signup_btn_xpath = "//button[normalize-space()='SIGN UP']"

    # login page
    email_inp_name = "email"
    password_inp_name = "password"
    login_btn_xpath = "//button[normalize-space()='LOGIN']"
    logout_btn_xpath = "//a[normalize-space()='Sign out']"

    def click_logo(self):
        self.driver.find_element(By.XPATH, self.click_logo()).click()

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.signup_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def signup(self, name, email, password):
        name_input = self.driver.find_element(By.ID, self.name_inp_id)
        email_input = self.driver.find_element(By.ID, self.email_inp_id)
        password_input = self.driver.find_element(By.ID, self.password_inp_id)
        send_text(name_input, name)
        send_text(email_input, email)
        send_text(password_input, password)
        self.driver.find_element(By.ID, self.tc_agree_id).click()
        self.driver.find_element(By.XPATH, self.signup_btn_xpath).click()

    def login(self, email, password):
        email_input = self.driver.find_element(By.NAME, self.email_inp_name)
        password_input = self.driver.find_element(By.NAME, self.password_inp_name)
        send_text(email_input, email)
        send_text(password_input, password)
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_btn_xpath)
