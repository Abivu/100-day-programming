import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 49.895138 # Your latitude
MY_LONG = -97.138374 # Your longitude
MY_EMAIL = "abi.vu117@gmail.com"
MY_PASSWORD = "rttl jpnh rjtr vmnz"


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, #Change to 24-hr format
}

def is_iss_close():
    '''
    The function to define whether iss is close to our current location - Winnipeg
    +/- 5 degrees of the ISS actual position 
    Output: return True/False
    '''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    

def is_night_time():
    '''
    The function to define whether or not it is a night time
    Output: return True/False
    '''
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    
while True:
    time.sleep(60)
    if is_iss_close() and is_night_time():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: look up!\n\nLook Up. ISS is coming close."
            )
    else:
        print("ISS is not close yet.")

# BONUS: run the code every 60 seconds.





