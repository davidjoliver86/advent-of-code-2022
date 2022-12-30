"""
Test cases for Day 12
"""
import re

from aoc2022 import day12

HILL = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()


def test_find_path():
    """
    Test that the shortest path above from S to E has 31 steps. The list will contain 32 elements including the start
    as the first "step", so subtract 1.
    """
    end_node = day12.find_path(HILL, (0, 0), (5, 2))
    assert len(end_node.path) - 1 == 31


def test_find_path_second_star():
    """
    Test that the among all 'a' starting points to E has 29 steps.
    """
    end_node = day12.find_path(HILL, (0, 4), (5, 2))
    assert len(end_node.path) - 1 == 29


def test_node_repr():
    """
    Test the __repr__ method of Node.
    """
    node = day12.Node(0, 0)
    assert re.match(r"Node<\(0,0\) @ 0x[0-9a-f]*>", repr(node))


def test_node_repr_with_prev():
    """
    Test the __repr__ method of Node where there is a previous node.
    """
    node = day12.Node(0, 0)
    node2 = day12.Node(1, 0, node)
    assert re.match(r"Node<\(0,1\) @ 0x[0-9a-f]*, prev 0x[0-9a-f]*>", repr(node2))


def test_first_star():
    """
    Test first star solution.
    """
    assert day12.first_star() == 394


def test_second_star():
    """
    Test second star solution.
    """
    assert day12.second_star() == 388
