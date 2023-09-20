##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random
import os


#1: Search in birthdays.csv 
df = pd.read_csv("./birthdays.csv")
# Compact data month and day into a tuple
today = (dt.datetime.now().month, dt.datetime.now().day)

# Loop through Dataframe using index attribute
# Dict comprehension at its finest - key is a tuple and value is a row of data
birthday_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today in birthday_dic:
    #2: Take the data of interest and replace in placeholders with the random template
    # To avoid hard coding and manually update the number of files in the file path
    file_count = len(os.listdir("./letter_templates/")) 
    choice = random.randint(1, file_count)
    # Randomly choose the letter template
    file_path = f"./letter_templates/letter_{choice}.txt"
    message = []

    # TODO: Not yet covering multiple birthdays on the same day
    birthday_person = birthday_dic[today]

    with open( file_path, "r") as birthday_card:
        content = birthday_card.readlines()
        first_line = content[0].replace("[NAME]", birthday_person["name"])
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
        to_addrs=birthday_person["email"],
        msg=f"Subject: Happy Birthday {birthday_person['name']}\n\n{message}"
    )