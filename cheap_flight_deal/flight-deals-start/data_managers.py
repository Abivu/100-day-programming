import requests

sheety_api_endpoint = "https://api.sheety.co/2626f983fd56b83b06f0c1db01dbd088/personalFlightDeals/prices"

sheety_headers = {
    "Content-Type": "application/json"
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def read_google_sheet(self):
        '''
        This function will read the sheet and return a dictionary of cities in the sheet
        that has Iata code is empty
        '''
        response = requests.get(url=sheety_api_endpoint, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()["prices"] # data is a list of dictionary
        empty_cities = {data.index(element)+2: element["city"] for element in data if element["iataCode"] == ""}
        return empty_cities # {3: 'Berlin', 4: 'Tokyo', 6: 'Istanbul', 7: 'Kuala Lumpur'}


    def write_google_sheet(self, list_empty_iata, empty_cities):
        '''
        The function will write a list of iata code into a row that has empty iata code
        Input: list of empty iata and dictionary of empty cities
        '''
        # !! Upgrade this function: call this function in order to update row by row 
        # in the google Sheet
        list_empty_cities = list(empty_cities.keys())
        for index in range(len(list_empty_iata)):
            object_id = str(list_empty_cities[index])
            paramaters = {
                    "price": {
                        "iataCode": list_empty_iata[index]
                    }
                }
            response = requests.put(url=sheety_api_endpoint+"/"+object_id, headers=sheety_headers,json=paramaters)
        print(response.status_code)
        

