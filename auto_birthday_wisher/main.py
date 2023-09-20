##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random
import os


#1: Search in birthdays.csv 
df = pd.read_csv("./birthdays.csv")
today = dt.datetime.now()

# Loop through Dataframe using index attribute
for i in df.index:
    month = df.month[i]
    day = df.day[i]
    if today.month == month and today.day == day:
        name = df.name[i]
        email_add = df.email[i]
    # Not yet covering multiple birthdays on the same day
#2: Take the data of interest and replace in placeholders with the random template
# To avoid hard coding and manually update the number of files in the file path
file_count = len(os.listdir("./letter_templates/")) 
choice = random.randint(1, file_count)
# Randomly choose the letter template
file_path = f"./letter_templates/letter_{choice}.txt"
message = []
with open( file_path, "r") as birthday_card:
    content = birthday_card.readlines()
    first_line = content[0].replace("[NAME]", name)
    message.append(first_line)
    for line in content[1:]:
        message.append(line)
    message = "".join(message)

#3: Connect to email & write script that if it satisfies the condition, an email would be sent out

my_email = "abi.vu117@gmail.com"
my_password = "" #Erase for security

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email_add,
        msg=f"Subject: Happy Birthday {name}\n\n{message}"
    )