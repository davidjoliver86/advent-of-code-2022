"""
Test cases for Day 2
"""
from aoc2022 import day2


def test_score_shape_strategy():
    """
    Test that the "second column means shape" strategy guide results in a score of 15.
    """
    assert day2.total_score("tests/fixtures/day2.txt", day2.second_column_means_shape) == 15


def test_score_outcome_strategy():
    """
    Test that the "second column means outcome" strategy guide results in a score of 15.
    """
    assert day2.total_score("tests/fixtures/day2.txt", day2.second_column_means_outcome) == 12


def test_first_star():
    """
    Test first star solution.
    """
    assert day2.first_star() == 13526


def test_second_star():
    """
    Test second star solution.
    """
    assert day2.second_star() == 14204
