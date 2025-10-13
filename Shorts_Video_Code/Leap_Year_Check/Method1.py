""" Using calendar Module """

import calendar

def is_leap(year):
    return calendar.isleap(year)

print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2024))