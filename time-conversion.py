#!/usr/bin/env python
'''
https://www.hackerrank.com/challenges/time-conversion

http://stackoverflow.com/questions/3453702/convert-12hr-date-time-string-to-24hr-datetime
'''

import datetime as dt
import dateutil.parser as dparser
import sys


time = raw_input().strip()


#date_str='on Jun 03, 02010 at 10:22PM'
date = dparser.parse(time)
#print(date)
# 2010-06-03 22:22:00
#print(date.strftime('%a, %d %b %Y %H:%M:%S'))
print(date.strftime('%H:%M:%S'))



