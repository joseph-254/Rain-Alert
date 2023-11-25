import requests
import os
from twilio.rest import Client


URL = "https://api.openweathermap.org/data/2.5/weather"
API_key = os.environ.get("OWM_API_Key")

account_sid = 'AC1fcd90d547165cd7d49930214538a8e1'
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": -1.292066,
    "lon": 36.821945,
    "appid": API_key

}

response = requests.get(URL, params=parameters)
# print(response.raise_for_status())
weather_data = response.json()


if weather_data["weather"][0]["id"] <= 500:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Make sure to carry your umbrella",
        from_='+15594729593',
        to='+254707544959'
    )
    print(message.status)
