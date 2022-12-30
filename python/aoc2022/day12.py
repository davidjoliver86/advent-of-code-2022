"""
Day 12: Hill Climbing Algorithm
"""
import dataclasses
from collections import deque
from string import ascii_lowercase
from typing import List, Optional, Self, Tuple

from aoc2022.utils import DIRS, lines


@dataclasses.dataclass
class Node:
    """
    Nodes represent a pair of coordinates with an optional link to the previous node.
    """

    col: int
    row: int
    prev: Optional[Self] = None

    def __repr__(self):
        if self.prev:
            return f"Node<({self.row},{self.col}) @ {hex(id(self))}, prev {hex(id(self.prev))}>"
        return f"Node<({self.row},{self.col}) @ {hex(id(self))}>"

    @property
    def location(self) -> Tuple[int, int]:
        """
        Returns:
            Tuple[int, int]: The location of this node in (Y, X) format.
        """
        return (self.col, self.row)

    @property
    def path(self) -> List[Tuple[int, int]]:
        """
        Recursively builds the path out from this node based on the previous node (and its previous node and so on).

        Returns:
            List[Tuple[int, int]]: A list of all steps in the path, including the start and end.
        """
        path = [self.location]
        if self.prev is None:
            return path
        return path + self.prev.path


def find_path(grid: List[str], start: Tuple[int, int], end: Tuple[int, int]) -> Node:
    """
    Breadth-first search for a valid path through the grid. Checks adjacent directions for valid directions, which
    in this case means any path of equal to or no greater than one "character" larger than the previous.

    Args:
        grid (List[str]): The grid to search through, as a list of strings.
        start (Tuple[int, int]): Starting coordinates.
        end (Tuple[int, int]): Ending coordinates.

    Returns:
        Node: The node representing the final step in the path.
    """
    heights = f"S{ascii_lowercase}E"
    queue = deque()
    seen = set()
    queue.append(Node(start[0], start[1], None))
    grid_height = len(grid)
    grid_length = len(grid[0])
    while queue:
        current = queue.popleft()
        if current.location in seen:
            continue
        seen.add(current.location)
        if current.location == end:
            return current
        char1 = grid[current.row][current.col]
        height1 = heights.index(char1)
        for d_y, d_x in DIRS:
            proposed = Node(current.col + d_x, current.row + d_y, current)
            valid = 0 <= proposed.row < grid_height and 0 <= proposed.col < grid_length
            if not valid:
                continue
            char2 = grid[proposed.row][proposed.col]
            height2 = heights.index(char2)
            if height2 <= height1 + 1:
                queue.append(proposed)


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The length of the shortest path from S to E.
    """
    grid = list(lines("fixtures/day12.txt"))
    start, end = None, None
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == "S":
                start = (col_index, row_index)
            if char == "E":
                end = (col_index, row_index)
    end_node = find_path(grid, start, end)
    return len(end_node.path) - 1


def second_star() -> int:
    """
    Second star solution.

    Here we sort of recreate a smaller version of our find_path function. In this case, we only want to find adjacent
    'a' characters next to 'S'. Once we have all of our potential 'a' or 'S' starting points, run them all through the
    pathfinding function and see which path winds up having the fewest steps.

    Returns:
        int: The number of steps in the path with the fewest steps.
    """
    grid = list(lines("fixtures/day12.txt"))
    grid_height = len(grid)
    grid_width = len(grid[0])
    start, end = None, None
    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == "S":
                start = (col_index, row_index)
            if char == "E":
                end = (col_index, row_index)

    # From the starting node, branch out and find all the other "a"'s adjacent to it.
    queue = deque()
    seen = set()
    queue.append(start)
    starting_points = set()
    starting_points.add(start)
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        for d_y, d_x in DIRS:
            proposed = (current[0] + d_x, current[1] + d_y)
            valid = 0 <= proposed[1] < grid_height and 0 <= proposed[0] < grid_width
            if not valid:
                continue
            if grid[proposed[1]][proposed[0]] == "a":
                queue.append(proposed)
                starting_points.add(proposed)

    # Run the find_path on all nodes.
    winner = None
    for starting_point in starting_points:
        end_node = find_path(grid, starting_point, end)
        if end_node:
            if winner is None or len(end_node.path) < len(winner.path):
                winner = end_node
    return len(winner.path) - 1


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
