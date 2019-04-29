import curses
from datetime import date, datetime, timedelta
import math
import time
import facts

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


CUR_DATE = date.today()
try:
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    stdscr.border(0)
    i = 0
    #while i <= 1:
        #to_p, result, res_type = find_date(CUR_DATE, i)
        #if res_type:
    #stdscr.addstr(5, 5, "str(i)", curses.A_BOLD)
    #i+=0.01
    #time.sleep(1)
    while i <= 1:
        to_p, result, res_type = find_date(CUR_DATE, i)
        stdscr.addstr(5, 5, (str(int(i*100)) + "%"), curses.A_BOLD)
        if res_type:
            pass
        else:
            if result > 8000:
                for key, value in facts.facts_ma.items():
                    if key > result:
                        to_p = str(value)
                        break
            else:
                year_bc = abs(CUR_DATE.year - result)
                for key, value in facts.facts_bc.items():
                    if key < year_bc:
                        to_p = str(value)
                        break
        stdscr.addstr(6, 5, (str(to_p) + " "*10), curses.A_BOLD)
        curses.doupdate()
        stdscr.refresh()
        i+=0.01
        time.sleep(0.03)
    stdscr.addstr(7, 5, 'Press q to close this screen', curses.A_NORMAL)
    while True:
        # stay in this loop till the user presses 'q'
        ch = stdscr.getch()
        if ch == ord('q'):
            break
    
finally:
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()
