"""
Test cases for Day 8
"""
import pytest

from aoc2022 import day8

SCENIC_SCORE_TEST_CASES = ((2, 1, 4), (2, 3, 8))


def test_count_vislble_trees():
    """
    Test that there are 21 visible trees in the example forest.
    """
    forest = day8.Forest("tests/fixtures/day8.txt")
    assert forest.count_visible_trees() == 21


@pytest.mark.parametrize("tree_x,tree_y,expected", SCENIC_SCORE_TEST_CASES)
def test_scenic_score(tree_x: int, tree_y: int, expected: int):
    """
    Tests that the provided scenic scores of the sample trees are as expected.

    Args:
        tree_x (int): The tree's x-coordinate.
        tree_y (int): The tree's y-coordinate.
        expected (int): The expected "scenic score" of that tree.
    """
    forest = day8.Forest("tests/fixtures/day8.txt")
    assert forest.tree_scenic_score(tree_x, tree_y) == expected


def test_first_star():
    """
    Test first star solution.
    """
    assert day8.first_star() == 1690


def test_second_star():
    """
    Test second star solution.
    """
    assert day8.second_star() == 535680
