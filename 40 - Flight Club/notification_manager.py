import smtplib
import os
from dotenv import load_dotenv

load_dotenv("example.env")

EMAIL = os.environ.get('EMAIL_SENDER')
PASSWORD = os.environ.get('EMAIL_SENDER_PASSWORD')


class NotificationManager:

    @staticmethod
    def send_email(user, message):
        """Send email to user"""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=user,
                msg=message
            )
