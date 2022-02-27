from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users_manager import Users

data_manager = DataManager()
# Get data on the sheet
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set Rio de Janeiro as the origin
ORIGIN_CITY_IATA = "RIO"

# Fill missing IATA codes
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Search flight for the destinations on sheet
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # If there is a flight and its price is lower than the one saved on the sheet: alert user
    if (flight is not None) and flight.price < destination["lowestPrice"]:
        users_data = Users.get_users_data()
        users_names = [row["firstName"] for row in users_data]
        users_emails = [row["email"] for row in users_data]
        for email in users_emails:
            notification_manager.send_email(
                message=f"Low price alert! Only R${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.",
                user=users_names[email.index()]
            )
