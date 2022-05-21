import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.453060  # Your latitude
MY_LONG = 18.537239  # Your longitude

MY_EMAIL = "bootbastick@yahoo.com"
PASSWORD = "pfcmbhhjtiionwcy"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


iss_latitude = float(data["iss_position"]["latitude"])
print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
while True:
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        if sunset <= int(time_now.strftime("%H")) < 24:
            if sunset < int(time_now.strftime("%H")):
                connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
                # connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="boikoff.nikita@gmail.com",
                                    msg=f"Subject:ISS is above you!\n\n"
                                        f"Look up and you will see an ISS!")
                connection.quit()
        else:
            if sunrise - int(time_now.strftime("%H")) > 0:
                connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
                # connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="boikoff.nikita@gmail.com",
                                    msg=f"Subject:ISS is above you!\n\n"
                                        f"Look up and you will see an ISS!")
                connection.quit()
    time.sleep(60)
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
