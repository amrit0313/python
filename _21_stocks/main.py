from pyexpat.errors import messages

import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API = "noyb"
URL = "https://www.alphavantage.co/query?"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY="key opens the door"

TWILIO_ACC = "see yours"
AUTH_TOKEN = "take fuckin yourself"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "apikey": API}
response = requests.get(URL, params=parameters)
data = response.json()["Time Series (Daily)"]
new_list = [values for (keys, values) in data.items()]
yesterdays_close = float(new_list[0]["4. close"])
previous_close = float(new_list[1]["4. close"])
percent = (yesterdays_close - previous_close) / yesterdays_close * 100
print(f"{percent}% ")
if percent >= 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "q":COMPANY_NAME,
        "searchIn":"title"
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = news_response.json()

    required_data = data["articles"][:3]
    format = [f"Headlines: {article['title']} . \n Brief: {article["description"]} \n"  for article in  required_data]

    client = Client(TWILIO_ACC, AUTH_TOKEN)
    for article in format:
        messages = client.messages.create(
            body= article,
            from_ ="+17856293822",
            to = "+9779848961396 "
        )

