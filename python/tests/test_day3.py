"""
Test cases for Day 3
"""
import pytest

from aoc2022 import day3


def test_sum_rucksack():
    """
    Test that the sum of the example rucksacks' duplicate item type priorities == 157.
    """
    assert day3.sum_rucksack("tests/fixtures/day3.txt") == 157


def test_no_dupe():
    """
    In case we were provided with a rucksack without a duplicate item, test that ValueError is thrown.
    """
    with pytest.raises(ValueError):
        day3.find_duplicate_item("abcd")


def test_priority_groups_of_three():
    """
    Test that the sum of the example rucksacks' set-of-three badge item type priorities == 70.
    """
    assert day3.priority_groups_of_three("tests/fixtures/day3.txt") == 70


def test_first_star():
    """
    Test first star solution.
    """
    assert day3.first_star() == 7795


def test_second_star():
    """
    Test second star solution.
    """
    assert day3.second_star() == 2703
