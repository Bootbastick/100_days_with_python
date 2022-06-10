import requests
import datetime
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_API_KEY = "*working API key*"

MY_EMAIL = "*bot email witch everybody can make*"
PASSWORD = "*password to bot email witch I don't need*"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY
}
stock_connection = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_connection.raise_for_status()
stock_data = stock_connection.json()["Time Series (Daily)"]

time_now = [int(datetime.datetime.now().strftime("%m")), int(datetime.datetime.now().strftime("%d"))]
stock_date_key_list = list(stock_data.keys())
yesterday_date = stock_date_key_list[0]




yesterday_stock_price = stock_data[yesterday_date]
yesterday_closing_stock_price = float(yesterday_stock_price["4. close"])

day_before_yesterday_date = stock_date_key_list[1]
day_before_yesterday_closing_stock_price = float(stock_data[day_before_yesterday_date]["4. close"])

difference = yesterday_closing_stock_price - day_before_yesterday_closing_stock_price
positive_difference = abs(difference)

percentage_difference = positive_difference / ((yesterday_closing_stock_price + day_before_yesterday_closing_stock_price) / 2)
true_percentage_difference = difference / ((yesterday_closing_stock_price + day_before_yesterday_closing_stock_price) / 2)

if percentage_difference > 0.05:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": "*working news API key*"
    }
    news_connection = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_params)
    news_connection.raise_for_status()
    news_data = news_connection.json()
    first_three_articles = [news_data["articles"][:2]]
    try:
        first_three_articles_dict = {
            first_three_articles[0][0]["title"]: first_three_articles[0][0]["description"],
            first_three_articles[0][1]["title"]: first_three_articles[0][1]["description"],
            first_three_articles[0][2]["title"]: first_three_articles[0][2]["description"]
        }
        first_three_articles_list = [
            first_three_articles[0][0]["title"],
            first_three_articles[0][1]["title"],
            first_three_articles[0][2]["title"]
        ]
    except IndexError:
        try:
            first_three_articles_dict = {
                first_three_articles[0][0]["title"]: first_three_articles[0][0]["description"],
                first_three_articles[0][1]["title"]: first_three_articles[0][1]["description"]
            }
            first_three_articles_list = [
                first_three_articles[0][0]["title"],
                first_three_articles[0][1]["title"],
            ]
        except IndexError:
            try:
                first_three_articles_dict = {
                    first_three_articles[0][0]["title"]: first_three_articles[0][0]["description"]
                }
                first_three_articles_list = [
                    first_three_articles[0][0]["title"],
                ]
            except IndexError:
                first_three_articles_dict = {}
                first_three_articles_list = []

    for i in range(0, 2):
        connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
        # connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        headline = first_three_articles_list[i]
        message = f"Subject:Stonks! {true_percentage_difference} change!\n\nHeadline:\n{headline}\nBriefing:\n{first_three_articles_dict[headline]}".encode()
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="*somebody's email*",
            msg=message
        )
        connection.quit()

