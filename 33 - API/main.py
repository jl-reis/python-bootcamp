import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv("example.env")

MY_LAT = int(os.environ.get('LAT'))  # Your latitude
MY_LONG = int(os.environ.get('LONG'))  # Your longitude
MY_EMAIL = os.environ.get('EMAIL_TEST')
MY_PASSWORD = os.environ.get('EMAIL_TEST_PASSWORD')

time_now = datetime.now()

while time_now.hour < 24:
    # Attribute actual time in each loop
    time_now = datetime.now()
    time.sleep(0.9)
    # Get ISS coordinates every minute
    if time_now.second == 0:

        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        # If my position is within +5 or -5 degrees of the ISS position.
        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:

            parameters = {
                "lat": MY_LAT,
                "lng": MY_LONG,
                "formatted": 0,
            }

            response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
            response.raise_for_status()
            data = response.json()
            sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
            sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

            # If my local time is nighttime
            if time_now.hour < sunrise or time_now.hour > sunset:
                send_to = "email@email.com"
                with smtplib.SMTP("https://smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=send_to,
                                        msg="Subject:ISS is passing near you!\n\n"
                                        f"Right now ({time_now.time()}) the ISS is passing at the coordinates:\n"
                                        f"Latitude: {iss_latitude}\nLongitude: {iss_longitude}"
                                        )
