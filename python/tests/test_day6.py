"""
Test cases for Day 6
"""
import pytest

from aoc2022 import day6

FIND_START_OF_PACKET_MARKER_TESTS = (
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ("ffaaiill", None),
)

FIND_START_OF_MESSAGE_MARKER_TESTS = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
)


@pytest.mark.parametrize("test_input,expected", FIND_START_OF_PACKET_MARKER_TESTS)
def test_find_start_packet_marker(test_input: str, expected: int):
    """
    Test cases for find_start_marker for the start-of-packet marker.

    Args:
        test_input (str): Sample input provided on the website.
        expected (int): Expected character number of first marker.
    """
    assert day6.find_start_marker(test_input, 4) == expected


@pytest.mark.parametrize("test_input,expected", FIND_START_OF_MESSAGE_MARKER_TESTS)
def test_find_start_message_marker(test_input: str, expected: int):
    """
    Test cases for find_start_marker for the start-of-message marker.

    Args:
        test_input (str): Sample input provided on the website.
        expected (int): Expected character number of first marker.
    """
    assert day6.find_start_marker(test_input, 14) == expected


def test_first_star():
    """
    Test first star solution.
    """
    assert day6.first_star() == 1300


def test_second_star():
    """
    Test second star solution.
    """
    assert day6.second_star() == 3986
