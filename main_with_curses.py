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

def ask(prompt, type_=None, min_=None, max_=None, range_=None):
    """Get user input of a certain type, with range and min/max options."""
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(
                        template.format(
                            " or ".join(
                                (
                                    ", ".join(map(str, range_[:-1])),
                                    str(range_[-1]),
                                )
                            )
                        )
                    )
        else:
            return ui



mins = ask("How long are you waiting for? (minutes) ", float, 0)
secs = mins*60
wait_time = secs/1000
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
        if i < 0.1:
            stdscr.addstr(5, 5, (str(int(i*100)) + "%" + " |" + "#"*int(i*20) + " "*(20-int(i*20)) + "|"), curses.A_BOLD)
        else:
            stdscr.addstr(5, 5, (str(int(i*100)) + "%" + "|" + "#"*int(i*20) + " "*(20-int(i*20)) + "|"), curses.A_BOLD)
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
                done = False
                for key, value in facts.facts_bc.items():
                    if key < year_bc:
                        to_p = str(value)
                        done = True
                        break
                if not done:
                    to_p = "No facts for this era."
        stdscr.addstr(6, 5, (str(to_p) + " "*13), curses.A_BOLD)
        curses.doupdate()
        stdscr.refresh()
        i+=0.001
        time.sleep(wait_time)
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
