"""
Test cases for Day 4
"""
from aoc2022 import day4


def test_full_containment():
    """
    Test that "full containment" in the example applies to only 2 shifts.
    """
    assert day4.count_shifts("tests/fixtures/day4.txt", day4.strategy_full_containment) == 2


def test_any_overlap():
    """
    Test that there are 4 shifts in the example with any overlap.
    """
    assert day4.count_shifts("tests/fixtures/day4.txt", day4.strategy_any_overlap) == 4


def test_first_star():
    """
    Test first star solution.
    """
    assert day4.first_star() == 573


def test_second_star():
    """
    Test second star solution.
    """
    assert day4.second_star() == 867
