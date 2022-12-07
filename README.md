# Advent of Code 2022

It's that time of year again. Featuring:

* Fedora 37 VM for development/testing. In its repos:
  * Python 3.11
  * Golang 1.19.3

Once again, code quality, readibility, and applicibility of best practices is the primary emphasis of the Python branch. I will similiarly try so with Golang as well, but cannot confidently promise as much in that area. Also, I am not necessarily going for "leaderboard cred", particularly since I had to miss the first few days anyway. Solving the puzzles and sticking to the standards is enough "cred" for me.

## Python conventions
* Code formatted with `black` (except with a 120-character line limit, deviating from the default 88).
* 10/10 Pylint with as few exceptions as possible. Exceptions must have justifications.
* Only Python code goes in the `aoc2022` folder. All puzzle input is saved in fixtures.
* Everything should be runnable as a module from within the `python` folder - e.g. `python -m aoc2022.day1`
* Unit tests that cover both the proposed sample cases *AND THE ACTUAL ANSWERS*.
* Enforcing 100% test coverage.
* Remember that your input is not necessarily going to match mine. That being said, tests will contain spoilers. Tread carefully.
