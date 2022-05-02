import random
import smtplib
import datetime as dt
import pandas

# Constants
MY_EMAIL = "bootbastick@yahoo.com"
PASSWORD = "pfcmbhhjtiionwcy"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    which_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{which_letter}.txt", mode="r") as file:
        file_red = file.read()
    letter = file_red.replace("[NAME]", birthdays_dict[today]["name"])

    connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
    # connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthdays_dict[today]["email"],
        msg=f"Subject:Happy Birthday!\n\n{letter}"
    )
    connection.quit()
