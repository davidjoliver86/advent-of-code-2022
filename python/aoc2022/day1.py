"""
Day 1: Calorie Counting
"""
from aoc2022 import utils


def sum_calories(path: str) -> list[int]:
    """
    Sums up the amount of calories each Elf is carrying. Add up numbers in consecutive lines; each Elf's calories are
    separated by a blank line.

    Args:
        path (str): Path to a text file of calorie data.

    Returns:
        list[int]: A list of each Elf's total calories in order.
    """
    data = utils.lines(path)
    calories = [0]
    for line in data:
        if line == "":
            calories.append(0)
        else:
            calories[-1] += int(line)
    return calories


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The number of calories carried by the Elf that carried the most.
    """
    calories = sum_calories("fixtures/day1.txt")
    return max(calories)


def second_star() -> int:
    """
    Seecond star solution.

    Returns:
        int: The total number of calories carried by the top three Elves.
    """
    calories = sum_calories("fixtures/day1.txt")
    return sum(sorted(calories, reverse=True)[:3])


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
