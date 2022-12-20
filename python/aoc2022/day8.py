"""
Day 8: Treetop Tree House
"""
from aoc2022 import utils


class Forest:
    """
    A forest represents a grid of trees. Each tree is an integer from 0-9 representing its height (or perhaps 0
    indicates the absense of a tree).
    """

    _trees: list[list[int]]
    _height: int
    _width: int

    def __init__(self, path: str):
        self._trees = []
        for line in utils.lines(path):
            self._trees.append([int(char) for char in line])

        # Cache width and height so we don't constantly recalculate them
        self._width = len(self._trees[0])
        self._height = len(self._trees)

    def _tree_visible(self, tree_x: int, tree_y: int) -> bool:
        """
        A tree is always visible if it is at the edge of the grid. Otherwise, a tree is considered visible if, for any
        of the four directions of the trees' line of sight, there is no tree of equal or greater height looking off in
        that direction.

        Args:
            tree_x (int): The tree's x-coordinate.
            tree_y (int): The tree's y-coordinate.

        Returns:
            bool: Whether the tree is considered visible.
        """
        # Is the tree at the edge?
        if tree_x == 0 or tree_y == 0 or tree_x == self._width - 1 or tree_y == self._height - 1:
            return True

        # Check left and right
        # Technically, left needs to be checked in reverse order, but since the condition must hold true for ALL trees,
        # it doesn't really matter in the end.
        row = self._trees[tree_y]
        value = row[tree_x]
        left = row[:tree_x]
        right = row[tree_x + 1 :]

        if all((tree < value for tree in left)):
            return True

        if all((tree < value for tree in right)):
            return True

        # Check above and below
        # Again, above needs to be checked in reverse order, but since the condition must hold true for ALL trees, it
        # doesn't really matter in the end.
        col = [row[tree_x] for row in self._trees]
        above = col[:tree_y]
        below = col[tree_y + 1 :]

        if all((tree < value for tree in above)):
            return True

        if all((tree < value for tree in below)):
            return True

        return False

    def tree_scenic_score(self, tree_x: int, tree_y: int) -> int:
        """
        The tree's scenic score represents the product of the number of trees visible across all four directions. Trees
        on the edge of the map are disregarded, and by proxy, have a "scenic score" of 0.

        Args:
            tree_x (int): The tree's x-coordinate.
            tree_y (int): The tree's y-coordinate.

        Returns:
            int: The product of how many trees are visible across all four directions.
        """
        # Is the tree at the edge?
        if tree_x == 0 or tree_y == 0 or tree_x == self._width - 1 or tree_y == self._height - 1:
            return 0

        # Extract variables (mainly left/right/above/below)
        row = self._trees[tree_y]
        this_tree = row[tree_x]
        left = row[:tree_x]
        right = row[tree_x + 1 :]
        col = [row[tree_x] for row in self._trees]
        above = col[:tree_y]
        below = col[tree_y + 1 :]

        # Declare loop enumeration variables to satisfy Pylint
        # Because we already know the tree is not at an edge, we know there are spaces in all four directions.
        left_score: int
        right_score: int
        above_score: int
        below_score: int

        # Looking left - the [::-1] ensures we start right and look leftward
        for left_score, tree in enumerate(left[::-1], start=1):
            if tree >= this_tree:
                break

        # Looking right
        for right_score, tree in enumerate(right, start=1):
            if tree >= this_tree:
                break

        # Looking above - the [::-1] ensures we start above and look upward
        for above_score, tree in enumerate(above[::-1], start=1):
            if tree >= this_tree:
                break

        # Looking below
        for below_score, tree in enumerate(below, start=1):
            if tree >= this_tree:
                break

        return left_score * right_score * above_score * below_score

    def count_visible_trees(self) -> int:
        """
        Returns:
            int: The number of trees in the forest that are considered visible (see _tree_visible()).
        """
        visible = 0
        for tree_y, row in enumerate(self._trees):
            for tree_x, _ in enumerate(row):
                if self._tree_visible(tree_x, tree_y):
                    visible += 1
        return visible

    def find_highest_scenic_score(self) -> int:
        """
        Returns:
            int: The highest scenic score among all trees in the forest (see tree_scenic_score()).
        """
        highest = self.tree_scenic_score(0, 0)
        for tree_y, row in enumerate(self._trees):
            for tree_x, _ in enumerate(row):
                highest = max(highest, self.tree_scenic_score(tree_x, tree_y))
        return highest


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: Number of visible trees from the provided input.
    """
    forest = Forest("fixtures/day8.txt")
    return forest.count_visible_trees()


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: Highest "scenic score" tree from the provided input.
    """
    forest = Forest("fixtures/day8.txt")
    return forest.find_highest_scenic_score()


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
