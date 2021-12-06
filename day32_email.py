'''import smtplib
my_email = "dotrungkien3c@gmail.com"
password = "0123698745"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password= password)
    connection.sendmail(from_addr=my_email, to_addrs="kien.dt182922@sis.hust.edu.vn",msg="Subject:Hello\n\n this is an email")
'''
'''import datetime as dt
now = dt.datetime.now()
print(now)
year = now.year
print(year)
print(now.month)
print(now.date())
date_of_birth = dt.datetime(year=2000,month=10,day=7,hour=4)
print(date_of_birth)'''

my_email = "dotrungkien3c@gmail.com"
password = "0123698745"
import smtplib
import  datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readline()
        quote =  random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email, to_addrs="kien.dt182922@sis.hust.edu.vn",
                            msg=f"Subject:Motivation\n\n {quote}")