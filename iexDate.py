import datetime
from datetime import date, timedelta

def thisweek() :
   return datetime.datetime.now().strftime("%W")

def previousworkday():
    today = date.today()
    weekday= int(today.strftime("%u"))
    if weekday == 7 :
        prevday = datetime.datetime.now() - timedelta(days= 2)
    elif weekday == 1 :
        prevday = datetime.datetime.now() - timedelta(days= 3)
    else :
        prevday = datetime.datetime.now() - timedelta(days= 1)
    dayofyear = prevday.strftime("%G%m%d")
    return dayofyear

