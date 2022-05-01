import time
from selenium.webdriver.common.by import By
from Utilities.common_method_2 import *


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    depart_from_inp = "//input[@id='BE_flight_origin_city']"
    going_to_inp = "//input[@id='BE_flight_arrival_city']"
    departure_date_inp = "//input[@id='BE_flight_origin_date']"
    return_date_inp = "//input[@id='BE_flight_arrival_date']"
    all_city_path = "//div[@class='viewport']//div[1]/li"
    all_date_path = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTd']"
    traveller_class = "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']"
    adults = "(//span[@class='ddSpinnerPlus'])[1]"
    senior_citizen = "//a[normalize-space()='Senior Citizen']"
    search_flights_btn = "(//input[@id='BE_flight_flsearch_btn'])[1]"

    def all_city(self):
        elements = self.driver.find_elements(By.XPATH, self.all_city_path)
        return elements

    def all_date(self):
        elements = self.driver.find_elements(By.XPATH, self.all_date_path)
        return elements

    def depart_from(self, city):
        self.driver.find_element(By.XPATH, self.depart_from_inp).click()
        time.sleep(1)
        select_city(self.all_city(), city)

    def going_to(self, city):
        self.driver.find_element(By.XPATH, self.going_to_inp).click()
        time.sleep(1)
        select_city(self.all_city(), city)

    def departure_date(self, date):
        self.driver.find_element(By.XPATH, self.departure_date_inp).click()
        select_date(self.all_date(), date)

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
