import requests
import smtplib

api_key = "api_key_here"
MY_LAT = 42.453060
MY_LONG = 18.537239
MY_EMAIL = "bootbastick@yahoo.com"
PASSWORD = "pfcmbhhjtiionwcy"


params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for i in range(12):
    weather_id = weather_data["hourly"][i]["weather"][0]["id"]
    if weather_id < 600:
        will_rain = True

if will_rain:
    print("Bring umbrella")
    connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
    # connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="boikoff.nikita@gmail.com",
                        msg="Subject: Bad weather\n\nToday's going to be rainy."
                            "Don't forget to bring an umbrella with you!")
