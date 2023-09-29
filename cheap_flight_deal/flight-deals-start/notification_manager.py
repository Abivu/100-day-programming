
from twilio.rest import Client
from dotenv import load_dotenv
from os import environ as env

load_dotenv()
account_sid = env["account_sid"]
auth_token = env["auth_token"]
client = Client(account_sid, auth_token)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, flight_price, departure_time, link_to_book, fly_to):


        message = client.messages.create(
        from_='+12563882868',
        to='+12046989527', 
        body=f"Low price alert! only EUR{flight_price}\n to fly from LON to {fly_to}\n\n at Departure time: {departure_time}\n\nCllick this link to book: {link_to_book}"
        )
        return message.status