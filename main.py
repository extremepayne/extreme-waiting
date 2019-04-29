from datetime import date, datetime, timedelta
import math
import time
import sys
import facts

CUR_DATE = date.today()
# print(CUR_DATE.year)


def decimal_year_to_date(decimal_year):
    """Change YYYY.YYYY to MM DD YYYY."""
    """Stack overflow 20911015"""
    year = int(decimal_year)
    rem = decimal_year - year
    base = datetime(year, 1, 1)
    out = base + timedelta(
        seconds=(base.replace(year=base.year + 1) - base).total_seconds() * rem
    )
    return out


def find_date(todays_date, progress):
    """Find a date according to XKCD 1017."""
    return_date = math.exp((20.3444 * (progress ** 3)) + 3) - math.exp(3)
    if return_date < todays_date.year:
        my_date = decimal_year_to_date(todays_date.year - return_date).date()
        return my_date.strftime("%B %d %Y"), my_date, True
    return str(round(return_date)) + " years ago", return_date, False


i = 0
while i <= 1:
    to_p, result, res_type = find_date(CUR_DATE, i)
    if res_type:
        to_p = str(int(i * 100)) + "%       " + to_p + "     \r"
        sys.stdout.write(to_p)
        sys.stdout.flush()
        time.sleep(0.03)
        i += 0.01
    else:
        if result > 8000:
            for key, value in facts.facts_ma.items():
                if key > result:
                    to_p = (
                        str(int(i * 100))
                        + "%"
                        + str(value)
                        + "              \r"
                    )
                    sys.stdout.write(to_p)
                    sys.stdout.flush()
                    break
            time.sleep(0.03)
            i += 0.0003
        else:
            year_bc = abs(CUR_DATE.year - result)
            for key, value in facts.facts_bc.items():
                if key < year_bc:
                    to_p = (
                        str(int(i * 100))
                        + "%"
                        + str(value)
                        + "              \r"
                    )
                    sys.stdout.write(to_p)
                    sys.stdout.flush()
                    break
            time.sleep(0.03)
            i += 0.0001
input("press enter to exit                       ")
