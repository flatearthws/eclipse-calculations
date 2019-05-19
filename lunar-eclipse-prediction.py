#!/usr/bin/env python
'''
lunar-eclipse-prediction.py

Shows the occurences of a lunar eclipse in the 21st century.
Works by iterating every hour in the 21st century and calculating if the
separation between the Moon and the Sun is more than 180°-0.9° (= 179.1°).
The number 0.9° is hardcoded for simplicity, for more accuracy, it
should be computed from the distance of the Moon and the Sun.
'''
import ephem
from datetime import datetime, timedelta

# start and end time
curtime = datetime(2001, 1, 1, 0, 0, 0)
endtime = datetime(2100, 12, 31, 23, 59, 59)

# initialize Moon, Sun & observer
moon = ephem.Moon()
sun = ephem.Sun()
observer = ephem.Observer()
observer.elevation = -6371000  # place the observer at the center of the Earth
observer.pressure = 0          # disable atmospheric refraction

# loop every hour
while curtime <= endtime:
    observer.date = curtime

    # computer the position of the sun and the moon with respect to the observer
    moon.compute(observer)
    sun.compute(observer)

    # calculate the separation between the moon and the sun, convert
    # it from radians to degrees, subtract it by 180°.
    # this is basically the separation of the moon from the Earth's
    # center of umbra.
    sep = abs((float(ephem.separation(moon, sun))
        / 0.01745329252) - 180)

    # eclipse occurs if the separation is less than 0.9°.
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
