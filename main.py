from datetime import date, datetime, timedelta
import math
import time

CUR_DATE = date.today()
# print(CUR_DATE.year)


def decimal_year_to_date(decimal_year):
    """Change YYYY.YYYY to MM DD YYYY."""
    """Stack overflow 20911015"""
    year = int(decimal_year)
    rem = decimal_year - year
    base = datetime(year, 1, 1)
    result = base + timedelta(
        seconds=(base.replace(year=base.year + 1) - base).total_seconds() * rem
    )
    return result


def find_date(todays_date, progress):
    """Find a date according to XKCD 1017."""
    return_date = math.exp((20.3444 * (progress ** 3)) + 3) - math.exp(3)
    if return_date < 2000:
        my_date = decimal_year_to_date(todays_date.year - return_date).date()
        return my_date.strftime("%B %d %Y")
    return str(round(return_date)) + " years ago"


i = 0
while i <= 1:
    print(find_date(CUR_DATE, i))
    time.sleep(0.1)
    i += 0.01
input("press enter to exit")
