import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from datetime import datetime

load_dotenv("example.env")

ACCOUNT_ID = os.environ.get("TWILIO_ID")
ACCOUNT_AUTH = os.environ.get("TWILIO_AUTH")
ACCOUNT_PHONE = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

API_KEY = os.environ.get("WEATHER_API_KEY")
PARAMS = {
    "lat": "-22.785950",
    "lon": "-43.313179",
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(API_ENDPOINT, params=PARAMS)
weather_data = response.json()
hourly_dict = weather_data["hourly"][:12]

time_now = datetime.now()

print(time_now.weekday())
if 1 <= time_now.weekday() <= 5:
    print("yes")
is_raining = True

for hour in hourly_dict:
    if hour["weather"][0]["id"] <= 700:
        is_raining = True

if is_raining:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(ACCOUNT_ID, ACCOUNT_AUTH, http_client=proxy_client)
    message = client.messages.create(
        body="Test message",
        from_=ACCOUNT_PHONE,
        to=MY_NUMBER
    )

    print("Bring an umbrella")
