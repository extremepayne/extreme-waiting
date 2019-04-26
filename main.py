from datetime import date
import math

CUR_DATE = date.today()
print(CUR_DATE.year)


def find_date(todays_date, progress):
    """Find a date according to XKCD 1017"""
    return math.exp((20.3444 * (progress ** 3)) + 3) - math.exp(3)


i = 1
while i <= 100:
    print(find_date(CUR_DATE.year, i))
    i += 1
input("press enter to exit")
