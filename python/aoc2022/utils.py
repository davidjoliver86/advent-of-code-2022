"""
General helper utilities
"""
import pathlib
from typing import Iterator

# Directional Constants
# Assuming a 2-dimensional "array", y-coordinates are the rows (the first index), and x-coordinates are the columns.

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = (UP, DOWN, LEFT, RIGHT)


def lines(path: str) -> Iterator[str]:
    """
    Reads a file and returns a list of its lines. Optionally accepts a callable, and if provided,
    applies that callable to all lines.
    Args:
        path (str): Path of the file to read.
    Yields:
        str: An iterable of those lines.
    """
    yield from pathlib.Path(path).read_text("utf-8").splitlines()
