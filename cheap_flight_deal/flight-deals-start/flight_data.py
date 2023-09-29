import requests

search_code_endpoint = "https://api.tequila.kiwi.com/locations/query"

headers = {
    "Content-Type": "application/json",
    "apikey": "HiMiQpOeZZWi2u7P_VIxUSiGvRb50RkJ"
}

class FlightData:
    # This class is responsible for structuring the flight data.
# list of empty_cities
    def search_for_iata(self, empty_cities):
        '''
        The function call api to extract iata code of the cities
        Input: a dictionary of cities having empty iata codes
        Output: a list of iata code with corresponding index of the dic empty_cities
        '''

        list_empty_cities = list(empty_cities.values())
        list_empty_iata = []
        for element in list_empty_cities:
            parameters = {
                "term": element,
                "location_types": "airport"
                }
            response = requests.get(url=search_code_endpoint, headers=headers, params=parameters)
            response.raise_for_status()
            iata_code = response.json()["locations"][0]["code"]
            list_empty_iata.append(iata_code)
        return list_empty_iata
