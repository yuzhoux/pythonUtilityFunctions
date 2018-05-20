#!/usr/bin/python

import sys
from datetime import datetime, timedelta

#Part 1
#Take variables from command lines
paramDict = {}
split_list = ''

for arg in sys.argv:
	split_list = arg.split("=")
	if len(split_list) > 1 :
		paramDict[split_list[0]] = split_list[1]	

with open(paramDict['file_name']) as f:
	query = f.read()

#Part 2
#Build frequently used calender dates, such as last day of three months ago
today=datetime.now()
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)
def monthdeltaA(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    return date.replace(day=1,month=m, year=y).strftime('%Y-%m-%d')
def monthdeltaB(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    return last_day_of_month(date.replace(day=1,month=m, year=y)).strftime('%Y-%m-%d')
def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    return date.replace(day=1,month=m, year=y).strftime('%Y-%m')
def weekdeltaA(date,delta):
    return (date+timedelta(days=7*delta)-timedelta(days=date.weekday())).strftime('%Y-%m-%d')
def weekdeltaB(date,delta):
    return (date+timedelta(days=7*delta)+timedelta(days=6)-timedelta(days=date.weekday())).strftime('%Y-%m-%d')

for m in range(-12, 13):
    paramDict['current_month'+str("%+d" % m)+'a']=monthdeltaA(today, m)
    paramDict['current_month'+str("%+d" % m)+'b']=monthdeltaB(today, m)
    paramDict['current_month'+str("%+d" % m)]=monthdelta(today, m)
for w in range(-4, 5):
    paramDict['current_week'+str("%+d" % w)+'a']=weekdeltaA(today, w)
    paramDict['current_week'+str("%+d" % w)+'b']=weekdeltaB(today, w)

#print(query.format(**paramDict)

#Part 3
#Run the same command for four times using the most recent four Sundays
dict={}
submit=" "

for w in range(-4, 0):
    dict['targetSunday']=weekdeltaB(today, w)
    submit=submit+'\n'+query.format(**dict)
#print(submit)

