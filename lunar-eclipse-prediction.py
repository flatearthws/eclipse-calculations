#!/usr/bin/env python
'''
lunar-eclipse-prediction.py

Shows the occurences of a lunar eclipse in the 21st century.
Works by iterating every hour in the 21st century and calculating if the
separation between the Moon and the Sun is less than 0.9° from 180°.
The number 0.9° is hardcoded for simplicity, for more accuracy, it
should be computed from the distance of the Moon and the Sun.
'''
import ephem
from datetime import datetime, timedelta

curtime = datetime(2001, 1, 1, 0, 0, 0)
endtime = datetime(2100, 12, 31, 23, 59, 59)
moon = ephem.Moon()
sun = ephem.Sun()
observer = ephem.Observer()
observer.elevation = -6371000
observer.pressure = 0

while curtime <= endtime:
    observer.date = curtime.strftime('%Y/%m/%d %H:%M:%S')

    moon.compute(observer)
    sun.compute(observer)
    sep = abs((float(ephem.separation(moon, sun))
        / 0.01745329252) - 180)

    if sep < 0.9:
        print(curtime.strftime('%Y/%m/%d %H:%M:%S'), sep)
        curtime += timedelta(days = 1)
    else:
        curtime += timedelta(hours = 1)
