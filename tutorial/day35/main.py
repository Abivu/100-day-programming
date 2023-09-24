import requests
from twilio.rest import Client
import os 

lat = -4.441931
long = 15.266293
api_key = os.environ.get("OWM_API_KEY")

## Twilio API
account_sid = 'AC4322edaf40ba4e3f6157c61230129ed6'
auth_token = os.environ.get("TWILIO_API_KEY")

paramaters = {
    "lat": lat,
    "lon":  long,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=paramaters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+12563882868',
    body='Bring an umbrella',
    to='+12046989527'
    )

print(message.sid)