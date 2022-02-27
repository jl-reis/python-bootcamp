import os
from dotenv import load_dotenv
import requests
from datetime import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

load_dotenv("example.env")

ACCOUNT_ID = os.environ.get("TWILIO_ID")
ACCOUNT_AUTH = os.environ.get("TWILIO_AUTH")
ACCOUNT_PHONE = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_API_ADDRESS = "https://www.alphavantage.co/query"

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ADDRESS = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

today = datetime.now().date()

news_params = {
    "q": COMPANY_NAME,
    "from": today,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": NEWS_API_KEY
}

stock_response = requests.get(STOCK_API_ADDRESS, params=stock_params)
tesla_data = stock_response.json()
data_keys = list(tesla_data.keys())
tesla_time_series = tesla_data[data_keys[1]]

time_series_keys = list(tesla_time_series.keys())

tesla_yesterday = tesla_time_series[time_series_keys[0]]
tesla_day_before = tesla_time_series[time_series_keys[1]]


# If the stock varies 5% or more
if not (0.95 * float(tesla_day_before["4. close"])) < float(tesla_yesterday["4. close"]) < \
        (1.05 * float(tesla_day_before["4. close"])):
    stock_percentage_variation = int(100 -
                                     (100 * (float(tesla_yesterday["4. close"]) / float(tesla_day_before["4. close"]))))
    if stock_percentage_variation > 0:
        stock_arrow = "🔺"
    else:
        stock_arrow = "🔻"
        stock_percentage_variation = abs(stock_percentage_variation)

    news_response = requests.get(NEWS_API_ADDRESS, params=news_params)
    news_data = news_response.json()

    alert_messages = []

    if not news_data["totalResults"]:
        if len(news_data["totalResults"]) >= 3:
            articles_data = news_data["articles"][:3]
            alert_messages = [f"{STOCK} {stock_arrow}{stock_percentage_variation}%\n"
                              f"Headline: {article['title']}\n"
                              f"Briefing: {article['description']}\n" for article in articles_data]

        else:
            articles_data = news_data["articles"]
            alert_messages = [f"{STOCK} {stock_arrow}{stock_percentage_variation}%\n"
                              f"Headline: {article['title']}\n"
                              f"Briefing: {article['description']}\n" for article in articles_data]
    else:
        alert_messages = [f"{STOCK} {stock_arrow}{stock_percentage_variation}%\n"
                          f"There are no news on radar. Get some info!"]

    for alert in alert_messages:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(ACCOUNT_ID, ACCOUNT_AUTH, http_client=proxy_client)
        message = client.messages.create(
            body=alert,
            from_=ACCOUNT_PHONE,
            to=MY_NUMBER
        )

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
