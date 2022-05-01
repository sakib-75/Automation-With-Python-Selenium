import pytest
from Pages.Pages_2.yatra_launch_page import HomePage


@pytest.mark.usefixtures("setup")
class TestSearchFlights:
    def test_search_flights(self):
        self.driver.get("https://www.yatra.com/")

        home = HomePage(self.driver)
        home.depart_from("Chennai (MAA)")
        home.going_to("Goa (GOI)")
        home.departure_date("12/05/2022")
        home.return_date("16/05/2022")
        home.traveller_class_click()
        home.adults_click(5)
        home.senior_citizen_click()
        home.search_flights_btn_click()
