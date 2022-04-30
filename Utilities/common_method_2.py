def select_city(all_city, city_name):
    for city in all_city:
        if city_name in city.text:
            city.click()
            break


def select_date(all_date, select_date):
    for date in all_date:
        if date.get_attribute("data-date") == select_date:
            date.click()
            break
