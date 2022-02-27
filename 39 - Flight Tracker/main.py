from data_manager import DataManager
from flight_search import FlightSearch
from users_manager import Users


sheet_entries = DataManager.get_entries()


def fill_iata_codes():
    """Fill the IATA codes missing in the sheet"""
    for entry in sheet_entries:
        if entry["iataCode"] == "":
            entry["iataCode"] = FlightSearch.search_location_iata(entry["city"])
        DataManager.insert_row(entry)


def search_flight():
    """Search flights to the cities in the sheet and saves the cheapest ones"""
    for entry in sheet_entries:
        actual_cheapest = FlightSearch.search_cheapest_flight_to(entry["iataCode"])
        if actual_cheapest != 0 and actual_cheapest < entry["lowestPrice"]:
            entry["lowestPrice"] = actual_cheapest
            DataManager.insert_row(entry)


Users.register_new_user()
