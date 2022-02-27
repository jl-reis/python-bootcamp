import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()

# Create question DB
question_data = []
for question in data["results"]:
    question_data.append(question)
