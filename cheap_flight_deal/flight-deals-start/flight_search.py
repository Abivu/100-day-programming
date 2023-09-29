import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
from os import environ as env
import json

load_dotenv()
search_flight_endpoint = "https://api.tequila.kiwi.com/v2/search"

today = dt.datetime.now()
six_months_later = today + relativedelta(months=6)

headers = {
    "Content-Type": "application/json",
    "apikey": env["apikey"]
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def search_for_flight(self, fly_to, price):
        parameters = {
            "fly_from": "LON",
            "fly_to": fly_to, 
            "date_from": today.strftime("%d/%m/%Y"), #str - format: dd/mm/yyyy
            "date_to": six_months_later.strftime("%d/%m/%Y"),
            "price_to": price #int
        }

        response = requests.get(url=search_flight_endpoint, headers=headers,params=parameters)
        response.raise_for_status()
        flights_data = response.json()["data"]
        try:
            if flights_data[0]:
                flight_price = flights_data[0]["price"]
                link_to_book = flights_data[0]["deep_link"]
                departure_time = flights_data[0]["local_departure"]
        except IndexError:
            self.search_for_flight()

        
        return flight_price, departure_time, link_to_book
    