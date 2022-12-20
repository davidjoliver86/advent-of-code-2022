"""
Day 9: Rope Bridge
"""
import dataclasses
from typing import Collection, Tuple

from aoc2022 import utils

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)
CARDINALS = (LEFT, RIGHT, UP, DOWN)
DIAGONALS = (UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)
ALL_DIRECTIONS = CARDINALS + DIAGONALS

Coordinates = Tuple[int, int]


def _add(coords1: Coordinates, coords2: Coordinates) -> Coordinates:
    """
    Adds two two-element tuples by adding their positional values together.
    For example: (1, 2) + (2, 3) = (3, 5).

    Args:
        coords1 (Coordinates): One addend.
        coords2 (Coordinates): The other addend.

    Returns:
        Coordinates: The result of adding each element.
    """
    return (coords1[0] + coords2[0], coords1[1] + coords2[1])


def _abs_diff(coords1: Coordinates, coords2: Coordinates) -> Coordinates:
    """
    Takes the difference of two two-element tuples and reduces the result to an absolute value descriptor.
    For either element:
        If c1 >  c2 -> 1.
        If c1 == c2 -> 0.
        If c1 <  c2 -> -1.

    Args:
        coords1 (Coordinates): One operand.
        coords2 (Coordinates): The other operand.

    Returns:
        Coordinates: The absolute value diff of each element.
    """
    raw_diff = (coords1[0] - coords2[0], coords1[1] - coords2[1])
    abs1 = -1 if raw_diff[0] < 0 else 0 if raw_diff[0] == 0 else 1
    abs2 = -1 if raw_diff[1] < 0 else 0 if raw_diff[1] == 0 else 1
    return (abs1, abs2)


@dataclasses.dataclass
class Knot:
    """
    Base class for all things that act like a Knot.
    """

    _position: Coordinates = (0, 0)

    def get_position(self) -> Coordinates:
        """
        Returns:
            Coordinates: This knot's current position.
        """
        return self._position


@dataclasses.dataclass
class Head(Knot):
    """
    Head represents the head knot of the rope.
    """

    _position: Coordinates = (0, 0)

    def move(self, direction: Coordinates):
        """
        Moves this head in the given direction.

        Args:
            direction (Coordinates): The direction to move.
        """
        self._position = _add(self._position, direction)


@dataclasses.dataclass
class Tail(Knot):
    """
    Tails represent the other knots in a rope. Their movement is dependent on the parent knot (either the head or
    another tail), and we also are interested in tracking the nodes each tail has visited.
    """

    _parent: Knot = None
    _visited: set(Coordinates) = None
    _position: Coordinates = (0, 0)

    def __init__(self, parent: Knot):
        super().__init__()
        self._parent = parent
        self._visited = {(0, 0)}

    def _move(self):
        parent_position = self._parent.get_position()

        # Is this tail touching its parent?
        for cmp_direction in ALL_DIRECTIONS:
            if _add(self._position, cmp_direction) == parent_position:
                return

        # If not, are they two steps away in a straight direction? If so, move tail one step that direction.
        for cmp_direction in CARDINALS:
            if _add(_add(self._position, cmp_direction), cmp_direction) == parent_position:
                self._position = _add(self._position, cmp_direction)
                return

        # Otherwise, move tail one step diagonally to keep up.
        best_direction = _abs_diff(parent_position, self._position)
        self._position = _add(self._position, best_direction)

    def move(self):
        """
        Moves this tail according to where it's currently located relative to its parent, then logs its location
        afterwards.
        """
        self._move()
        self._visited.add(self._position)

    def get_visitations(self) -> Collection[Coordinates]:
        """
        Returns:
            Collection[Coordinates]: A set of all coordinates this tail has touched.
        """
        return self._visited


class RopeGrid:
    """
    An abstract 2D space where Heads and Tails are free to move about.
    """

    _head: Coordinates
    _turns: int
    _tails: list(Coordinates)

    def __init__(self, path: str, tails: int = 1):
        self._head = Head()
        self._turns = 0
        self._num_tails = tails
        self._tails = []
        for line in utils.lines(path):
            direction, times = line.split()
            direction = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}[direction]
            times = int(times)
            for _ in range(times):
                self.move(direction)

    def move(self, direction: Coordinates):
        """
        Move the head in the provided direction. The tail will follow according to the rules of its movement.

        Args:
            direction (Coordinates): The direction to move the head.
        """
        # First, move head in direction.
        self._head.move(direction)

        # Increment turns counter and add a knot if turns <= knots.
        self._turns += 1
        if self._turns <= self._num_tails:
            parent = self._head if not self._tails else self._tails[-1]
            self._tails.append(Tail(parent))

        for tail in self._tails:
            tail.move()

    def get_tail_visitations(self, tail_number: int = 0) -> Collection[Coordinates]:
        """
        Returns for the provided tail number (index of self._tails) a set of coordinates touched.

        Args:
            tail_number (int, optional): Tail number index. Defaults to 0.

        Returns:
            Collection[Coordinates]: A set of all coordinates this tail has touched.
        """
        return self._tails[tail_number].get_visitations()


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The number of unique grid spaces the tail has visited.
    """
    grid = RopeGrid("fixtures/day9.txt")
    tail_visitations = grid.get_tail_visitations()
    return len(tail_visitations)


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: The number of unique grid spaces the ninth tail has visited.
    """
    grid = RopeGrid("fixtures/day9.txt", 9)
    tail_visitations = grid.get_tail_visitations(8)
    return len(tail_visitations)


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
