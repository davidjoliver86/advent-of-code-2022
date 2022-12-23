"""
Day 11: Monkey in the Middle
"""
import collections
import dataclasses
import operator
import re
from functools import partial, reduce
from typing import Callable

from aoc2022 import utils

Throw = collections.namedtuple("Throw", "recipient,worry_level")

# Function constructors for squaring, multiplication, and addition.
# These functions are expected to take in the current item's worry level and transform it.


def square(num: int) -> int:
    """
    Args:
        num (int): The number to square.

    Returns:
        int: The square of num. Treated as a unary operation given that <num> is expected to be the worry level.
    """
    return num**2


def add(num: int) -> Callable[[int], int]:
    """
    Args:
        num (int): The number to add.

    Returns:
        Callable[[int], int]: A function that returns the value passed to it plus <num>.
    """
    return partial(operator.add, num)


def multiply(num: int) -> Callable[[int], int]:
    """
    Args:
        num (int): The number to multiply.

    Returns:
        Callable[[int], int]: A function that returns the value passed to it times <num>.
    """
    return partial(operator.mul, num)


@dataclasses.dataclass
class Monkey:
    """
    Monkeys handle baggage and create anxiety for our worried traveler.

    Raises:
        ValueError: If the operation isn't addition, multiplication, or squaring.
    """

    operation: Callable
    test_divisible: int
    test_true: int
    test_false: int
    items: list[int] = dataclasses.field(default_factory=list)
    inspections_done: int = 0

    def __init__(self, instructions: str):
        # Starting items
        starting_items_str = re.search(r"Starting items: ([\d+].*)  Operation", instructions).group(1)
        self.items = [int(num) for num in starting_items_str.split(", ")]

        # Operation
        operation_str = re.search(r"Operation: new = (old . (\d+|old))", instructions).group(1)
        operator_str, operand = operation_str.split()[1:]
        if operator_str == "*" and operand == "old":
            self.operation = square
        elif operator_str == "*":
            self.operation = multiply(int(operand))
        elif operator_str == "+":
            self.operation = add(int(operand))
        else:
            raise ValueError("Unsupported operation")

        # Test
        test_str = re.search(r"Test: divisible by (\d+)", instructions).group(1)
        self.test_divisible = int(test_str)

        # Test true
        test_true_str = re.search(r"If true: throw to monkey (\d+)", instructions).group(1)
        self.test_true = int(test_true_str)

        # Test false
        test_false_str = re.search(r"If false: throw to monkey (\d+)", instructions).group(1)
        self.test_false = int(test_false_str)

    def catch_item(self, worry_level: int):
        """
        Catches an item thrown to it by another monkey - in other words, adds it to the end of self.items.

        Args:
            worry_level (int): Worry level of the item.
        """
        self.items.append(worry_level)

    def take_turn(self, divide_3: bool) -> list[Throw]:
        """
        Takes its turn by processing all the items in its items list, then determing what items to throw to other
        monkeys.

        Args:
            divide_3 (bool): First star specific - determines if worry levels are automatically divided by 3.

        Returns:
            list[Throw]: List of items to throw - specifically to which monkey, and what the worry level is.
        """
        items_to_throw = []
        for item in self.items:
            self.inspections_done += 1
            if divide_3:
                worry_level = self.operation(item)
            else:
                worry_level = self.operation(item) // 3
            test = worry_level % self.test_divisible == 0
            if test:
                items_to_throw.append(Throw(self.test_true, worry_level))
            else:
                items_to_throw.append(Throw(self.test_false, worry_level))
        self.items = []
        return items_to_throw


def make_monkeys(path: str) -> list[Monkey]:
    """
    Parses a text file of instructions and creates monkeys out of that.

    Args:
        path (str): Path to the text file.

    Returns:
        list[Monkey]: A list of monkeys created from the instructions.
    """
    lines = list(utils.lines(path))
    index = 0
    instruction_list = [""]
    for line in lines:
        if line == "":
            instruction_list.append("")
            index += 1
        else:
            instruction_list[index] += line
    monkeys = [Monkey(instructions) for instructions in instruction_list]
    return monkeys


def play_round(monkeys: list[Monkey], divide_3: bool):
    """
    Simulates one round of monkeys taking their turn, then throwing items to other monkeys.

    Args:
        monkeys (list[Monkey]): The monkeys.
        divide_3 (bool): First-star specific: whether to divide each items' worry level by 3.
    """
    for monkey in monkeys:
        items_to_throw = monkey.take_turn(divide_3)
        for item in items_to_throw:
            monkeys[item.recipient].catch_item(item.worry_level)


def calculate_monkey_business(monkeys: list[Monkey]) -> int:
    """
    Takes the two most active monkeys in terms of number of items inspected. Multiplies the result of each monkeys'
    total items inspected.

    Args:
        monkeys (list[Monkey]): The monkeys.

    Returns:
        int: The amount of "monkey business" between the top two.
    """
    inspections = sorted([monkey.inspections_done for monkey in monkeys], reverse=True)
    return inspections[0] * inspections[1]


def reduce_to_lcm(monkeys: list[Monkey], lcm: int):
    """
    Ensures the second star doesn't cause massive overflows. Reduces each monkey's item worry levels to the modulus
    of the LCM of each monkey's divisibility test factors.

    Args:
        monkeys (list[Monkey]): The monkeys.
        lcm (int): The LCM of each monkeys' divisibility test factors.
    """
    for monkey in monkeys:
        for index, item in enumerate(monkey.items):
            monkey.items[index] = item % lcm


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The amount of monkey business after 20 rounds.
    """
    monkeys = make_monkeys("fixtures/day11.txt")
    for _ in range(20):
        play_round(monkeys, False)
    return calculate_monkey_business(monkeys)


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: The amount of monkey business after 10,000 rounds, without automatically dividing worry levels by 3.
    """
    monkeys = make_monkeys("fixtures/day11.txt")
    lcm = reduce(operator.mul, [monkey.test_divisible for monkey in monkeys])
    for _ in range(10000):
        play_round(monkeys, True)
        reduce_to_lcm(monkeys, lcm)
    return calculate_monkey_business(monkeys)


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
