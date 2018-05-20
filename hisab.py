#!/usr/bin/env python
'''
Script untuk memperhitungkan 
'''
import ephem
from datetime import datetime, timedelta

curtime = datetime(2000, 1, 1, 5, 0, 0)        # start time
endtime = datetime(2020, 12, 1, 5, 0, 0)        # end time

moon = ephem.Moon()
sun = ephem.Sun()

observer = ephem.Observer()
observer.lon = '106.816667'
observer.lat = '-6.2'
observer.elevation = 8
yesterdayalt = 0

while curtime <= endtime:
    observer.date = curtime
    sunsettime = observer.next_setting(sun)
    observer.date = sunsettime
    moon.compute(observer)
    alt = float(moon.alt) / 0.01745329252
    if alt > 0 and yesterdayalt <= 0:
        if alt > 3:
            print("%s-%s-%s: Masuk bulan baru. Ketinggian bulan: %s°" % (curtime.year, curtime.month, curtime.day, alt))
        else:
            print("%s-%s-%s: Muhammadiyah masuk bulan baru, pemerintah tergantung rukyat. Ketinggian bulan: %s°" % (curtime.year, curtime.month, curtime.day, alt))

    yesterdayalt = alt
    curtime += timedelta(days = 1)