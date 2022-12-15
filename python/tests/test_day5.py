"""
Test cases for Day 5
"""
from aoc2022 import day5


def test_crate_mover_9000():
    """
    Test the functionality of the CrateMover 9000 which moves crates one at a time.
    """
    crates = day5.CrateMover9000("tests/fixtures/day5.txt")
    assert crates.get_top_crates() == ["C", "M", "Z"]


def test_crate_mover_9001():
    """
    Test the functionality of the CrateMover 9001 which moves many crates at a time.
    """
    crates = day5.CrateMover9001("tests/fixtures/day5.txt")
    assert crates.get_top_crates() == ["M", "C", "D"]


def test_first_star():
    """
    Test first star solution.
    """
    assert day5.first_star() == "RTGWZTHLD"


def test_second_star():
    """
    Test second star solution.
    """
    assert day5.second_star() == "STHGRZZFR"
