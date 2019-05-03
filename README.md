# extreme-waiting
> Make waiting an extreme sport! Swoosh!

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## What
This program takes a percentage and converts it to a date. As the percentage increases, the date goes back in time exponentially. This helps alleviate boredom caused by waiting.

## How
Run the appropriate version of main.py. (main_with_curses if your system supports curses package, main otherwise.) Enter the amount of time you have to wait for. It will display a percent (and a progress bar, for main_with_curses) and a date and/or significant events on or near that date.

### Curses
Curses is used to interact better with the terminal and allows this project to be better about printing things out. If `main.py` says it's not supported, here are some things you can try:

#### Unix
It should always work. File an issue.

#### Linux
Make sure ncurses is installed. Some distros pre-install it, others might not.

#### Windows
`pip install windows-curses`

#### MacOS
I don't have a Mac to try things on, so I don't know if you can do it. If you figure this out, PRs are welcome to fix or document support.

## Why
[xkcd 1017](https://xkcd.com/1017)

## Who
Licensed by extremepayne, 2019. See license.txt for more details.
