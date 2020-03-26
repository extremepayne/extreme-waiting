# extreme-waiting
> Make waiting an extreme sport! Swoosh!

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) ![GitHub top language](https://img.shields.io/github/languages/top/extremepayne/extreme-waiting.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## What
This program takes a percentage and converts it to a date. As the percentage increases, the date goes back in time exponentially. 
This helps alleviate boredom caused by waiting.

![example image](images/example.JPG)

## How
Run `main_with_curses.py`.

Enter the amount of time you have to wait for. It will display a percent and a date and/or significant events on or near that date.

### Curses
Curses is used to interact better with the terminal and allows this project to be better about printing things out. 
If `main_with_curses.py` says it's not supported, here are some things you can try:

#### Linux
Make sure ncurses is installed. Some distros pre-install it, others might not.

#### Windows
`pip install windows-curses`

## Why
[xkcd 1017](https://xkcd.com/1017)

## Who
Licensed by extremepayne, 2019. See license.txt for more details.
