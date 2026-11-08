from datetime import datetime, date

print(datetime.now())    # 2026-09-30 14:35:10.123456
print(date.today())      # 2026-09-30


#Get parts of a date

now = datetime.now()
print(now.year)     # 2026
print(now.month)    # 9
print(now.day)      # 30
print(now.hour)     # 14

#Create a specific date

d = datetime(2026, 12, 25, 10, 30)
print(d)   # 2026-12-25 10:30:00

#Format a date (date to text)

print(now.strftime("%d-%m-%Y"))       # 30-09-2026
print(now.strftime("%I:%M %p"))       # 02:35 PM
print(now.strftime("%A, %B %d"))      # Wednesday, September 30

#Read a date (text to date)

d = datetime.strptime("25-12-2026", "%d-%m-%Y")


import os
current_dir= os.getcwd()
print(current_dir)

