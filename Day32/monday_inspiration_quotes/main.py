import random
import smtplib
import datetime as dt

MY_EMAIL = "bootbastick@yahoo.com"
PASSWORD = "pfcmbhhjtiionwcy"

with open("quotes.txt", "r") as file:
    quotes = (file.readlines())

weekday = dt.datetime.now().weekday()
if weekday == 0:
    quote = random.choice(quotes)
    connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
    # connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="sergsv03@gmail.com", msg=f"Subject:Motivation\n\n{quote}")
    connection.quit()









# now = dt.datetime.now()
# year = now.year
#
# print(year)


