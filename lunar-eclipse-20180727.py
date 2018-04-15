#!/usr/bin/env python
'''
lunar-eclipse-20180727.py

A simple python script to calculate the separation of
the Moon from the center of Earth's umbra. When the
separation is the lowest, then it is the peak of the eclipse.

This is for the lunar eclipse on July 27, 2018
'''

import ephem
from datetime import datetime, timedelta

curtime = datetime(2018, 7, 27, 15, 0, 0)
endtime = datetime(2018, 7, 28, 0, 0, 0)
resdelta = timedelta(seconds = 60)   # resolution

moon = ephem.Moon()
sun = ephem.Sun()
observer = ephem.Observer()
observer.elevation = -6371000  # place observer in the center of the Earth
observer.pressure = 0          # disable refraction

while curtime <= endtime:
    observer.date = curtime.strftime('%Y/%m/%d %H:%M:%S')

    # computer the position of the sun and the moon with respect to the observer
    moon.compute(observer)
    sun.compute(observer)

    # calculate separation between the moon and the sun, convert
    # it from radians to degrees, substract it by 180°
    sep = abs((float(ephem.separation(moon, sun))
        / 0.01745329252) - 180)

    print(curtime.strftime('%Y/%m/%d %H:%M:%S'), sep)

    # advance by time interval defined in resdelta
    curtime += resdelta
