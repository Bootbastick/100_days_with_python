import smtplib

class NotificationManager:
    def __init__(self):
        self.MY_EMAIL = "bootbastick@yahoo.com"
        self.PASSWORD = "pfcmbhhjtiionwcy"
    def send_notification(self, user_email, text):
        connection = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
        # connection.starttls()
        connection.login(user=self.MY_EMAIL, password=self.PASSWORD)
        connection.sendmail(
            from_addr=self.MY_EMAIL,
            to_addrs=user_email,
            msg=f"Subject:We found a flight!\n\n{text}"
        )
        connection.quit()