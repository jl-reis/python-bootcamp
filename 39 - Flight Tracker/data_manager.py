# This class is responsible for talking to the Google Sheet.
import requests
import os
from dotenv import load_dotenv

load_dotenv("example.env")

SHEETY_API_ENDPOINT = "https://api.sheety.co/ce5c978854eff05451ef0a1842b8f961/flightDeals/prices"
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_HEADER = {
    "Authorization": SHEETY_AUTH
}


class DataManager:

    @staticmethod
    def get_entries():
        """Get entries from sheet"""
        sheety_response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADER)
        entries = sheety_response.json()["prices"]
        return entries

    @staticmethod
    def insert_row(entry):
        """Insert info in the sheet"""
        row = entry['id']
        entry["real"] = f'=GOOGLEFINANCE("CURRENCY:EURBRL")*C{row}'
        entry = {
            "price": entry
            }
        insert_response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{row}", headers=SHEETY_HEADER, json=entry)
        print(insert_response.text)
