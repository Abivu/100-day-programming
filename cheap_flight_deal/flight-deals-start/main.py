#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_managers import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet = DataManager()

empty_cities = sheet.read_new_cities()

search_iata = FlightData()
list_empty_iata = search_iata.search_for_iata(empty_cities)

if list_empty_iata is not None:
    sheet.write_google_sheet(list_empty_iata, empty_cities)

cities_of_interests = sheet.read_google_sheet()

# print(cities_of_interests)
deal_search = FlightSearch()
message = NotificationManager()
for element in cities_of_interests: #Each flight deal will be sent in a seoarate nessage
    fly_to = element["iataCode"]
    price = element["lowestPrice"]
    flight_price, departure_time, link_to_book = deal_search.search_for_flight(fly_to=fly_to, price=price)
    message.send_message(flight_price, departure_time, link_to_book, fly_to)

