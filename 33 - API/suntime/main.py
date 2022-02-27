import requests

lat = -17.594870
long = -68.548222

parameters = {
    "lat": lat,
    "lng": long,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

print(data)
