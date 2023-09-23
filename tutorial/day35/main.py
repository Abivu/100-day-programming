import requests

lat = 49.895138
long = -97.138374
api_key = "d2b203a1904118c205f7e16eda40d692"

paramaters = {
    "lat": lat,
    "lon":  long,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=paramaters)
# response.raise_for_status()
# print(response.status_code)
data = response.json()
print(data)