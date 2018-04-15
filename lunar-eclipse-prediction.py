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

curtime = datetime(2001, 1, 1, 0, 0, 0)        # start time
endtime = datetime(2100, 12, 31, 23, 59, 59)   # end time
moon = ephem.Moon()
sun = ephem.Sun()
observer = ephem.Observer()
observer.elevation = -6371000    # place observer in the center of the Earth
observer.pressure = 0            # disable refraction

while curtime <= endtime:
    observer.date = curtime.strftime('%Y/%m/%d %H:%M:%S')

    # computer the position of the sun and the moon with respect to the observer
    moon.compute(observer)
    sun.compute(observer)

    # calculate separation between the moon and the sun, convert
    # it from radians to degrees, substract it by 180°
    sep = abs((float(ephem.separation(moon, sun))
        / 0.01745329252) - 180)

    # eclipse happens if Sun-Earth-Moon alignment is less than 0.9°.
    # this should detect all total and partial eclipses, but is
    # hit-and-miss for penumbral eclipses.
    # the number is hardcoded for simplicity. for accuracy it should
    # be computed from the distance to the Sun and the Moon.
    if sep < 0.9:
        print(curtime.strftime('%Y/%m/%d %H:%M:%S'), sep)
        # an eclipse cannot happen more than once in a day,
        # so we skip 24 hours when an eclipse is found
        curtime += timedelta(days = 1)
    else:
        # advance an hour if eclipse is not found
        curtime += timedelta(hours = 1)
