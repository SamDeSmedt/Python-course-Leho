#!/usr/bin/python3
# Script that prints specified days

import datetime

Cdate = datetime.datetime.now() # Current day
DPdate = datetime.timedelta(days=7) #Delta Plus date
DMdate = datetime.timedelta(days=5) #Delta min date
Ndate = Cdate + DPdate
Udate= Cdate - DMdate

print(
    "Current date: {}\n"\
    "Date next week: {}\n"\
    "Five days before: {}"\
    .format(Cdate.strftime("%Y-%m-%d"), Ndate.strftime("%Y-%m-%d"), Udate.strftime("%Y-%m-%d"))
)