"""
Test cases for Day 9
"""
from aoc2022 import day9


def test_movement_with_one_tail():
    """
    Test that there should be 13 unique spaces the tail visited, including the starting point.
    For purposes of sanity, let's also check that the spaces match exactly what they should be:

    -4|..##..
    -3|...##.
    -2|.####.
    -1|....#.
     0|s###..
      -------
       012345
    """
    grid = day9.RopeGrid("tests/fixtures/day9.txt")
    tail_visited = grid.get_tail_visitations()
    assert tail_visited == set(
        (
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, -1),
            (1, -2),
            (2, -2),
            (3, -2),
            (4, -2),
            (3, -3),
            (4, -3),
            (2, -4),
            (3, -4),
        )
    )


def test_movement_with_nine_tails():
    """
    Test that there should be 36 unique spaces visited in a larger grid with 9 tails.
    """
    grid = day9.RopeGrid("tests/fixtures/day9-part2.txt", 9)
    tail_visited = grid.get_tail_visitations(8)
    assert len(tail_visited) == 36


def test_first_star():
    """
    Test first star solution.
    """
    assert day9.first_star() == 6011


def test_second_star():
    """
    Test second star solution.
    """
    assert day9.second_star() == 2419
