import requests
import os
from dotenv import load_dotenv

load_dotenv('example.env')

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ce5c978854eff05451ef0a1842b8f961/flightDeals/prices"
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_HEADER = {
    "Authorization": SHEETY_AUTH
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Get entries from sheet"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers= SHEETY_HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Update the IATA code in the sheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADER
            )
            print(response.text)
