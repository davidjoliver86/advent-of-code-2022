"""
Day 4: Camp Cleanup
"""
import re
from typing import Callable

from aoc2022 import utils


def strategy_full_containment(p1_start: int, p1_end: int, p2_start: int, p2_end: int) -> bool:
    """
    Strategy function. Given two ranges, determine if one range is fully contained within the other range. It doesn't
    matter which range covers which, just return whether or not one does.
    The data assumes p1_start < p1_end and p2_start < p2_end.

    Args:
        p1_start (int): Start of range 1.
        p1_end (int): End of range 1.
        p2_start (int): Start of range 2.
        p2_end (int): End of range 2.

    Returns:
        bool: Whether the provided ranges have one range fully contained by the other.
    """
    return (p1_start <= p2_start and p1_end >= p2_end) or (p2_start <= p1_start and p2_end >= p1_end)


def strategy_any_overlap(p1_start: int, p1_end: int, p2_start: int, p2_end: int) -> bool:
    """
    Strategy function. Given two ranges, determine if there is any overlap at all between the two.
    The data assumes p1_start < p1_end and p2_start < p2_end.

    This is determined by finding if there is any intersection of numbers between the two ranges.

    Args:
        p1_start (int): Start of range 1.
        p1_end (int): End of range 1.
        p2_start (int): Start of range 2.
        p2_end (int): End of range 2.

    Returns:
        bool: Whether the provided ranges have any overlap at all.
    """
    return bool(set(range(p1_start, p1_end + 1)) & set(range(p2_start, p2_end + 1)))


def count_shifts(path: str, strategy: Callable[[int, int, int, int], bool]) -> int:
    """
    Given a text file and a strategy function, return the number of lines that satisfy that strategy function.

    Args:
        path (str): Path to the file of shift assignments.
        strategy (Callable[[int, int, int, int], bool]): A strategy function.

    Returns:
        int: Number of lines that pass the strategy function.
    """
    count = 0
    for line in utils.lines(path):
        p1_start, p1_end, p2_start, p2_end = (int(match) for match in re.findall(r"\d+", line))
        if strategy(p1_start, p1_end, p2_start, p2_end):
            count += 1
    return count


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: Number of assignment pairs with fully contained shift assignments.
    """
    return count_shifts("fixtures/day4.txt", strategy_full_containment)


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: Number of assignment pairs with any overlap at all.
    """
    return count_shifts("fixtures/day4.txt", strategy_any_overlap)


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
