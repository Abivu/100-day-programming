#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_managers import DataManager
from flight_data import FlightData

sheet = DataManager()
# empty_cities = sheet.read_gooogle_sheet()
empty_cities = sheet.read_google_sheet()
# print(empty_cities)

search_iata = FlightData()
list_empty_iata = search_iata.search_for_iata(empty_cities)
# print(list_empty_iata)

sheet.write_google_sheet(list_empty_iata, empty_cities)