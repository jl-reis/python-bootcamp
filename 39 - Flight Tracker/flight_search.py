import requests
import datetime as datetime
import os
from dotenv import load_dotenv

load_dotenv("example.env")

FLIGHT_SEARCH_API_KEY = os.environ.get("FLIGHT_SEARCH_API_KEY")
FLIGHT_SEARCH_API_HEADER = {
    "apikey": FLIGHT_SEARCH_API_KEY
}
FLIGHT_SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    @staticmethod
    def search_location_iata(info):
        """Search IATA code for the city"""
        params = {
            "term": info
        }

        search_location_response = requests.get(url=f"{FLIGHT_SEARCH_API_ENDPOINT}locations/query",
                                                headers=FLIGHT_SEARCH_API_HEADER,
                                                params=params)
        return search_location_response.json()["locations"][0]["code"]

    @staticmethod
    def search_cheapest_flight_to(city):
        """Search the cheapest flight to city in the next 6 months"""
        today = datetime.date.today()
        delta = datetime.timedelta(days=1)
        trip_date = today + delta
        delta = datetime.timedelta(days=180)
        return_date = today + delta
        params = {
            "fly_from": "RIO",
            "fly_to": city,
            "date_from": trip_date.strftime("%d/%m/%Y"),
            "date_to": return_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "BRL"
        }

        search_flight_response = requests.get(url=f"{FLIGHT_SEARCH_API_ENDPOINT}v2/search",
                                              params=params, headers=FLIGHT_SEARCH_API_HEADER)
        all_search_flight_data = search_flight_response.json()
        try:
            flight_fare = all_search_flight_data["data"][0]["price"]
        except:
            flight_fare = 0

        return flight_fare
