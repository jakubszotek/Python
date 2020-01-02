# Working with dates and time
from datetime import date, time, datetime
 
today_var = date.today()
print(today_var)
 
# Components of a date
print(today_var.day)
print(today_var.month)
print(today_var.year)
print(today_var.weekday())  # 0 for Monday, 6 for Sunday
print(today_var.fromordinal)
#-------------------
 
# Date + time
now_var = datetime.now()
print(now_var)
 
# Just time
t = datetime.time(now_var)
print(t)
#-------------------
 
# Formatting date and time
print(now_var.strftime('The current year is %y'))   # last two digits of year
print(now_var.strftime('The current year is %Y'))   # year
print(now_var.strftime('The current month is %b'))   # 3-chracter month
print(now_var.strftime('The current month is %B'))   # full month string
print(now_var.strftime('The current day is %d'))   # day of month
print(now_var.strftime('The current weekday is %a'))   # 3-chracter weekday
print(now_var.strftime('The current weekday is %A'))   # full weekday string
 
print(now_var.strftime('The current full day and time is %c'))   # full day and time from local settings
print(now_var.strftime('The current full day is %x'))   # full date from local settings
print(now_var.strftime('The current time is %X'))   # time from local settings
 
print(now_var.strftime('The current full time is %I:%M:%S %p'))   # full time (12H + ... + am/pm)
print(now_var.strftime('The current full time is %H:%M:%S'))   # full time (24H)
print(now_var.strftime('The current time is %X'))   # time from local settings
#-------------------
 
 
# Task 1
# Create a function that would present the current date and time in the following manner
# assuming that the current date and time is   Mon Dec 23 12:29:09 2019:
# Today is Moday, 23 December 2019, the current time is 12 hours, 29 minutes and 9 seconds.
def present_current():
    now_var = datetime.now()
   

#check
present_current()
#-------------------


# Working with diferrences in dates and time
from datetime import timedelta
 
# what will be the date and time in one year?
print(now_var + timedelta(days=365))
 
# what will be the date and time in 5 weeks?
print(now_var + timedelta(weeks=5))
 
# negative values are also allowed
print(now_var + timedelta(weeks=-5, days=3, hours=-4))
 
 
# How many days are left until the next 1 June?
June1st = date(today_var.year, 6, 1)
if today_var > June1st:
    print("It was %d days ago." % ((today_var-June1st).days))
    June1st = June1st.replace(year = today_var.year + 1)
print("Next time it will be in %d days." % ((June1st-today_var).days))