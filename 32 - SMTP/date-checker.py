import smtplib
import datetime as dt
from random import choice

email_1 = "rafaelangelinooooo@gmail.com"
password = "aei1234#"

now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt") as data_file:
        quotes = data_file.readlines()

    email_text = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_1, password=password)
        connection.sendmail(from_addr=email_1, to_addrs="joao.lucas.reis@gmail.com", msg=f"Subject:Good Week!\n\n"
                                                                                         f"{email_text}")
        connection.close()
