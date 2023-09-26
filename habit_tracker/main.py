import requests
from requests.auth import HTTPBasicAuth
import os
import datetime as dt

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 160
AGE = 31

headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"],
    "Content-Type": "application/json"
}

exercise_tracking_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_tracking_endpoint, headers=headers, json=query)

workout_data = response.json()["exercises"][0]

now = dt.datetime.now()


workout_tracking_endpoint = "https://api.sheety.co/2626f983fd56b83b06f0c1db01dbd088/abi'sWorkouts/workouts"
basic = HTTPBasicAuth("abivu", os.environ["PASSWORD"])

json_logging = {
    "workout": 
    {
        "date": now.strftime("%d/%m/%Y") ,
        "time": now.strftime("%X"),
        "exercise": workout_data["user_input"],
        "duration": workout_data["duration_min"],
        "calories": workout_data["nf_calories"]
        }
}

headers = {
    "Content-Type": "application/json",
    "Authorization": os.environ["AUTHORIZATION"]
}

response = requests.post(url=workout_tracking_endpoint, json=json_logging, headers=headers, auth=basic)
print(response.status_code)
