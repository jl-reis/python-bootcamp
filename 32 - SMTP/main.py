import smtplib
import pandas as pd
import random
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv("example.env")

EMAIL_SENDER = os.environ.get('EMAIL_TEST')
PASSWORD_SENDER = os.environ.get('EMAIL_TEST_PASSWORD')

now = dt.datetime.now()

birthdays_df = pd.read_csv("birthdays.csv")

for index,  friend in birthdays_df.iterrows():
    if friend['month'] == now.month and friend['day'] == now.day:
        random_letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_letter}.txt") as letter_file:
            letter = letter_file.read()
        letter_with_name = letter.replace("[NAME]", friend['name'].capitalize())
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL_SENDER, PASSWORD_SENDER)
            connection.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs="email@email.com",
                msg=f"Subject:Happy Birthday!\n\n{letter_with_name}"
            )


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




