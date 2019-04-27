from datetime import date, datetime, timedelta
import math

CUR_DATE = date.today()
print(CUR_DATE.year)


def find_date(todays_date, progress):
    """Find a date according to XKCD 1017"""
    return_date = math.exp((20.3444 * (progress ** 3)) + 3) - math.exp(3)
    if return_date < 2000:
        return todays_date.year - return_date
    return return_date


i = 0
while i <= 1:
    print(find_date(CUR_DATE, i))
    i += 0.01
input("press enter to exit")
