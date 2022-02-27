import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("example.env")

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
NLP_HEADERS = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY"),
    "x-remote-user-id": "0"
}
NLP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/ce5c978854eff05451ef0a1842b8f961/myWorkouts/workouts"
SHEETY_HEADERS = {
    "Authorization": os.environ.get("SHEETY_BEARER")
}

# Get exercise info from user
body = {
    "query": input("What did you do today?\n"),
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

# Get NLP analyses from API
nlp_response = requests.post(url=NLP_ENDPOINT, json=body, headers=NLP_HEADERS)

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M")

entries = nlp_response.json()

for entry in entries["exercises"]:
    exercise = entry["name"].title()
    duration = entry["duration_min"]
    calories = entry["nf_calories"]

    exercise_json = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=exercise_json, headers=SHEETY_HEADERS)


