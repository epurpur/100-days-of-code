from datetime import datetime
from datetime import date
from datetime import timedelta

print (datetime.today())
today = datetime.today()
print (type(today))         #datetime objects

todaydate = date.today()

print (type(todaydate))     #date object. only date string, no extra time on end

print (todaydate.month)
print (todaydate.day)
print (todaydate.year)

christmas = (2018, 12, 25)  #assigning date to a variable
print (christmas)

t = timedelta(days = 4, hours = 10)
print (type(t))             #timedelta object
print (t.days)
print (t.seconds)           #10 hours, not seconds in days. only able to go up to maximum of 24 hours

print (t.seconds/60/60)     #60 minutes in an hour, 60 seconds in a minute

eta = timedelta(hours=20)
today = datetime.today()

print (today + eta)

print (str(today + eta))