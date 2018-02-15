#!/usr/bin/env python
import ephem
from datetime import datetime, timedelta

starttime = datetime(2018, 1, 31, 10, 0, 0)
endtime = datetime(2018, 1, 31, 17, 0, 0)
resdelta = timedelta(seconds = 300)

curtime = starttime
moon = ephem.Moon()
sun = ephem.Sun()

while curtime <= endtime:
    curtimes = curtime.strftime('%Y/%m/%d %H:%M:%S')

    observer = ephem.Observer()
    observer.lon = 0
    observer.lat = 0
    observer.elevation = -6371000
    observer.date = curtimes
    observer.temp = -272
    observer.pressure = 0

    moon.compute(observer)
    sun.compute(observer)
    sep = abs((float(ephem.separation(moon, sun)) / 0.01745329252) - 180)

    print(curtimes, sep)

    curtime += resdelta
