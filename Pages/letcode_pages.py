from selenium.webdriver.common.by import By
from Utilities.common_method_1 import send_text


class LetcodePages:
    def __init__(self, driver):
        self.driver = driver

    # home page
    signup_link = (By.XPATH, "//a[normalize-space()='Sign up']")
    login_link = (By.XPATH, "//a[normalize-space()='Log in']")

    # signup page
    name_inp = (By.ID, "name")
    email_inp = (By.ID, "email")
    password_inp = (By.ID, "pass")
    tc_agree = (By.ID, "agree")
    signup_btn = (By.XPATH, "//button[normalize-space()='SIGN UP']")

    # login page
    login_email_inp = (By.NAME, "email")
    login_password_inp = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[normalize-space()='LOGIN']")
    logout_btn = (By.XPATH, "//a[normalize-space()='Sign out']")

    def click_signup(self):
        self.driver.find_element(*self.signup_link).click()

    def click_login(self):
        self.driver.find_element(*self.login_link).click()

    def signup(self, name, email, password):
        name_input = self.driver.find_element(*self.name_inp)
        email_input = self.driver.find_element(*self.email_inp)
        password_input = self.driver.find_element(*self.password_inp)
        send_text(name_input, name)
        send_text(email_input, email)
        send_text(password_input, password)
        self.driver.find_element(*self.tc_agree).click()
        self.driver.find_element(*self.signup_btn).click()

    def login(self, email, password):
        email_input = self.driver.find_element(*self.login_email_inp)
        password_input = self.driver.find_element(*self.login_password_inp)
        send_text(email_input, email)
        send_text(password_input, password)
        self.driver.find_element(*self.login_btn).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_btn)
