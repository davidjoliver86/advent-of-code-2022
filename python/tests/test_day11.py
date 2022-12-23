"""
Test cases for Day 11
"""
import functools
from operator import mul

import pytest

from aoc2022 import day11


def test_monkey_business_first_star():
    """
    Test that the "monkey business" after 20 rounds is 10,605.
    """
    monkeys = day11.make_monkeys("tests/fixtures/day11.txt")
    for _ in range(20):
        day11.play_round(monkeys, False)
    assert day11.calculate_monkey_business(monkeys) == 10_605


def test_monkey_business_second_star():
    """
    Test that the "monkey business" after 10,000 rounds is 2,713,310,158, also keeping in mind not to automatically
    divide worry levels by 3.
    """
    monkeys = day11.make_monkeys("tests/fixtures/day11.txt")
    lcm = functools.reduce(mul, [monkey.test_divisible for monkey in monkeys])
    for _ in range(10000):
        day11.play_round(monkeys, True)
        day11.reduce_to_lcm(monkeys, lcm)
    assert day11.calculate_monkey_business(monkeys) == 2_713_310_158


def test_bad_monkey_operation():
    """
    Tests that an invalid operation throws ValueError.
    """
    with pytest.raises(ValueError):
        day11.make_monkeys("tests/fixtures/day11_bad.txt")


def test_first_star():
    """
    Test first star solution.
    """
    assert day11.first_star() == 113220


def test_second_star():
    """
    Test second star solution.
    """
    assert day11.second_star() == 30599555965
