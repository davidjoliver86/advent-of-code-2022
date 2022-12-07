"""
Test cases for Day 1
"""
from aoc2022 import day1


def test_sum_calories():
    """
    Test that the sum_calories() function returns 24000 from the test data.
    """
    calories = day1.sum_calories("tests/fixtures/day1.txt")
    assert max(calories) == 24000


def test_top_three_elf_calories():
    """
    Test that the total calories from the top three Elves total 45000.
    """
    calories = day1.sum_calories("tests/fixtures/day1.txt")
    assert sum(sorted(calories, reverse=True)[:3]) == 45000


def test_first_star():
    """
    Determine the Elf that is carrying the most calories. Return the number of calories.
    """
    assert day1.first_star() == 68442


def test_second_star():
    """
    Determine the top three Elves by calorie-carrying capacity. Return the total number of calories among them.
    """
    assert day1.second_star() == 204837
