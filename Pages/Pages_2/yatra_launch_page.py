import time
from selenium.webdriver.common.by import By
from Utilities.common_method_2 import *


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.depart_from_inp = "//input[@id='BE_flight_origin_city']"
        self.going_to_inp = "//input[@id='BE_flight_arrival_city']"
        self.departure_date_inp = "//input[@id='BE_flight_origin_date']"
        self.return_date_inp = "//input[@id='BE_flight_arrival_date']"
        self.all_city_path = "//div[@class='viewport']//div[1]/li"
        self.all_date_path = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTd']"
        self.traveller_class = "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']"
        self.adults = "(//span[@class='ddSpinnerPlus'])[1]"
        self.senior_citizen = "//a[normalize-space()='Senior Citizen']"
        self.search_flights_btn = "(//input[@id='BE_flight_flsearch_btn'])[1]"

    def all_city(self):
        elements = self.driver.find_elements(By.XPATH, self.all_city_path)
        return elements

    def all_date(self):
        elements = self.driver.find_elements(By.XPATH, self.all_date_path)
        return elements

    def depart_from(self, city):
        self.driver.find_element(By.XPATH, self.depart_from_inp).click()
        select_city(self.all_city(), city)
        time.sleep(1)

    def going_to(self, city):
        self.driver.find_element(By.XPATH, self.going_to_inp).click()
        select_city(self.all_city(), city)
        time.sleep(1)

    def departure_date(self, date):
        self.driver.find_element(By.XPATH, self.departure_date_inp).click()
        select_date(self.all_date(), date)
        time.sleep(1)

    def return_date(self, date):
        self.driver.find_element(By.XPATH, self.return_date_inp).click()
        select_date(self.all_date(), date)

    def traveller_class_click(self):
        self.driver.find_element(By.XPATH, self.traveller_class).click()

    def adults_click(self, click_time):
        for click in range(1, click_time):
            self.driver.find_element(By.XPATH, self.adults).click()

    def senior_citizen_click(self):
        self.driver.find_element(By.XPATH, self.senior_citizen).click()

    def search_flights_btn_click(self):
        self.driver.find_element(By.XPATH, self.search_flights_btn).click()
        time.sleep(2)
