import requests
from twilio.rest import Client

ACC_SID = "Your Twilio Account's SID"
AUTH_TOKEN = "Your Twilio Account's AUTH TOKEN"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters_for_stocks = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "your API Key",
}

parameters_for_news = {
    "qInTitle": "Tesla",
    "apiKey": "your API Key",
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_for_stocks)
response_stock.raise_for_status()
data_stock = response_stock.json()

time_series = data_stock["Time Series (Daily)"]
dates = sorted(time_series.keys(), reverse=True)
yesterday = float(time_series[dates[0]]["4. close"])
before_yesterday = float(time_series[dates[1]]["4. close"])

difference = (yesterday - before_yesterday)
up_down = None
if difference > 0:
    up_down = "Rise"
if difference < 0:
    up_down = "Fall"

percentage = round((difference/yesterday)*100,1)

if abs(percentage) >= 1:

    response_news = requests.get(url=NEWS_ENDPOINT, params=parameters_for_news)
    response_news.raise_for_status()
    articles = response_news.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK}: {percentage}% {up_down}\nHeadline:{article['title']}." for article in three_articles]

    client = Client(ACC_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="Your Twilio Number",
            to="Your Personal Number"
        )
        print(message.status)
