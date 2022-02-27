import requests
import os
from dotenv import load_dotenv

load_dotenv("example.env")

SHEETY_API_ENDPOINT = "https://api.sheety.co/ce5c978854eff05451ef0a1842b8f961/flightDeals/users"
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_HEADER = {
    "Authorization": SHEETY_AUTH
}


class Users:

    @staticmethod
    def register_new_user():
        """Register a new user"""
        print("Welcome to the Flight Club!\nWe find the best flights for you")
        user_first_name = input("What is your first name?\n")
        user_last_name = input("What is your last name?\n")
        user_email = input("What is your email?\n")

        entry = {
            "user": {
                "firstName": user_first_name,
                "lastName": user_last_name,
                "email": user_email
            }
        }

        register_response = requests.post(url=SHEETY_API_ENDPOINT, json=entry, headers=SHEETY_HEADER)
        print(register_response.text)
