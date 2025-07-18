'''

Date & Time

'''

# Uses system clock
import datetime

# Applies a specific date
date = datetime.date(2025, 1,23)
print(date)

# Prints the current system date
today = datetime.date.today()
print(today)

# Passing in a specific time
time = datetime.time(21,30,0)
print(time)

# Passing in a specific time
time = datetime.time(21,30,0)
print(time)

# Gets the current system time
now = datetime.datetime.now()
print(now)

# Using the strftime method for format a given date & time. https://strftime.org/
now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

# Check to see if a date & time has passed.
target_datetime = datetime.datetime(2000, 1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")



