from pprint import pprint
import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "my email"
PASSWORD = "password"
URL = "https://www.amazon.com/Zojirushi-NS-LGC05XB-Cooker-uncooked-Stainless/dp/B01EVHWNVG/ref=sr_1_10?crid=2CLZPMZQKI4GE&keywords=rice+cooker&qid=1647106860&sprefix=rice+cooker%2Caps%2C75&sr=8-10"

headers = {
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8,hr;q=0.7,sr;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
website_html = response.text
pprint(website_html)

soup = BeautifulSoup(website_html, "html.parser")

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = float(price_whole + "." + price_fraction)

if price < 200:
    connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
    # connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="boikoff.nikita@gmail.com",
        msg=f"Subject:Your product is cheaper!\n\nYour product on Amazon({URL}) right now is {price} euro! Buy now!"
    )
    connection.quit()
