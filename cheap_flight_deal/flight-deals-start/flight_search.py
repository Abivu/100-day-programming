import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import json

search_flight_endpoint = "https://api.tequila.kiwi.com/v2/search"

today = dt.datetime.now()
six_months_later = today + relativedelta(months=6)

headers = {
    "Content-Type": "application/json",
    "apikey": "HiMiQpOeZZWi2u7P_VIxUSiGvRb50RkJ"
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def search_for_flight(self, fly_to, price):
        parameters = {
            "fly_from": "LON",
            "fly_to": fly_to, 
            "date_from": today.strftime("%d/%m/%Y"), #str - format: dd/mm/yyyy
            "date_to": six_months_later.strftime("%d/%m/%Y"),
            "price_from": int(price - price*0.1), #int
            "price_to": int(price + price*0.1), #int
        }

        response = requests.get(url=search_flight_endpoint, headers=headers,params=parameters)
        response.raise_for_status()
        flights_data = response.json()["data"]
        try:
            if flights_data[0]:
                flight_price = flights_data[0]["price"]
                link_to_book = flights_data[0]["deep_link"]
        except IndexError:
            self.search_for_flight()

        
        return flight_price, link_to_book
