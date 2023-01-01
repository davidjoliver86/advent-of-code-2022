"""
Test cases for Day 13
"""
from typing import List, Tuple

import pytest

from aoc2022 import day13

MERGESORT_EXPECTED = [
    [],
    [[]],
    [[[]]],
    [1, 1, 3, 1, 1],
    [1, 1, 5, 1, 1],
    [[1], [2, 3, 4]],
    [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
    [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
    [[1], 4],
    [3],
    [[4, 4], 4, 4],
    [[4, 4], 4, 4, 4],
    [7, 7, 7],
    [7, 7, 7, 7],
    [[8, 7, 6]],
    [9],
]


def _test_params() -> List[Tuple[day13.Packet, day13.Packet, bool]]:
    """
    Helper function to generate test parameters for test_in_order().

    Returns:
        _type_: _description_
    """
    lists = day13.read_packets("tests/fixtures/day13.txt")
    expected = (True, True, False, True, False, True, False, False)
    return [(lists[0], lists[1], expected) for lists, expected in zip(lists, expected)]


@pytest.mark.parametrize("left,right,expected", _test_params())
def test_in_order(left: day13.Packet, right: day13.Packet, expected: bool):
    """
    Tests that the order checking function works as intended.

    Args:
        left (day13.Packet): The "left" packet to compare.
        right (day13.Packet): The "right" packet to compare.
        expected (bool): The expected result.
    """
    assert day13.in_order(left, right) == expected


def test_sorting():
    """
    Test the implementation of merge sort.
    """
    lists = day13.read_packets("tests/fixtures/day13.txt")
    flattened = []
    while lists:
        pair = lists.pop()
        while pair:
            flattened.append(pair.pop())
    ordered = day13.merge_sort(flattened)
    assert ordered == MERGESORT_EXPECTED


def test_packet_insertion():
    """
    Predicated on merge sort working, test that the addition of [[2]] and [[6]] result in a decoder key of 140.
    """
    lists = day13.read_packets_without_pairs("tests/fixtures/day13.txt")
    lists.append([[2]])
    lists.append([[6]])
    ordered = day13.merge_sort(lists)
    assert (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1) == 140


def test_first_star():
    """
    Test first star solution.
    """
    assert day13.first_star() == 5013


def test_second_star():
    """
    Test second star solution.
    """
    assert day13.second_star() == 25038
