"""
Day 3: Rucksack Reorganization
"""
import pathlib
import string

# By padding a space, this allows the index of the letter to correspond exactly to the items' priority.
PRIORITIES = " " + string.ascii_lowercase + string.ascii_uppercase


def find_duplicate_item(rucksack: str) -> str:
    """
    Given a "rucksack", determine the one item type that exists in both components of the rucksack.

    Args:
        rucksack (str): A string of the rucksack.

    Returns:
        str: The letter of the item type appearing in both compartments.
    """
    cutoff = len(rucksack) // 2
    left, right = rucksack[:cutoff], rucksack[cutoff:]
    for letter in left:
        if letter in right:
            return letter
    raise ValueError("A duplicate item was not found. This shouldn't happen.")


def get_priority(letter: str) -> int:
    """
    Given a letter of the item type, determine its "priority".

    Args:
        letter (str): The letter of the item type.

    Returns:
        int: The item type's "priority".
    """
    return PRIORITIES.index(letter)


def sum_rucksack(path: str) -> int:
    """
    Given a text file with a set of rucksacks, determine the duplicate item type priorities from each of them, then
    return the sum of them all.

    Args:
        path (str): The file containing rucksacks.

    Returns:
        int: The total "duplicate item type" priorities of all the rucksacks in the file.
    """
    items = [find_duplicate_item(rucksack) for rucksack in pathlib.Path(path).read_text(encoding="utf-8").splitlines()]
    priorities = [get_priority(item) for item in items]
    return sum(priorities)


def priority_groups_of_three(path: str) -> int:
    """
    Reading three lines at a time, find the one item type common among all three - their "common badge".
    (Techically, all lines are read; it only does a calculation on every third).

    Sum up the priorities of these common badges and return the result.

    Args:
        path (str): The file containing rucksacks.

    Returns:
        int: The total of each set-of-threes' common badge item type priorities.
    """
    with pathlib.Path(path).open("r", encoding="utf-8") as file:
        sacks = [None, None, None]
        priority_total = 0
        for index, line in enumerate(file):
            mod = index % 3
            sacks[mod] = line.strip()
            if mod == 2:
                common_badge = (set(sacks[0]) & set(sacks[1]) & set(sacks[2])).pop()
                priority_total += get_priority(common_badge)
    return priority_total


def first_star() -> int:
    """
    First star solution. Sum up all "duplicate item types" from the provided input.

    Returns:
        int: Total of all "duplicate item type" priorities.
    """
    return sum_rucksack("fixtures/day3.txt")


def second_star() -> int:
    """
    Second star solution. Sum up all sets-of-three common badge item type priorities.

    Returns:
        int: Total of all the badge priorities.
    """
    return priority_groups_of_three("fixtures/day3.txt")


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
