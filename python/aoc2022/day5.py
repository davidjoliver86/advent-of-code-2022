"""
Day 5: Supply Stacks
"""
import re
from collections import defaultdict

from aoc2022 import utils


class CrateMover9000:
    """
    The CrateMover 9000 is capable of moving a single crate at a time from one stack to another.
    """

    crates: dict = None
    instructions: list = None

    def __init__(self, path: str):
        """
        Initialize the crates and the instruction sequence to move them.

        The first part are the crates. As we encounter the letters, take the index of those letters and insert them as
        the first element of a list. The first element represents the bottom of the stack, so as more letters are added
        for that stack, the first letter winds up being the last element representing the top. For instance:

             [D]
        [N]  [C]
        [Z]  [M]  [P]
         1    2    3

        Results in lists of ["Z", "N"], ["M", "C", "D"], and ["P"] respectively.

        As soon as we reach a line starting with " 1", the indices of the characters on each line are translated into
        their 1-indexed form as stack numbers. So the final form of the crates becomes:
        {
            1: ["Z", "N"],
            2: ["M", "C", "D"]
            3: ["P"]
        }

        Then the file consists of commands in the form of "move X from Y to Z". We'll store those for now and deal with
        them eventually, but ultimately those are commands to move X number of boxes from stack number Y onto stack Z.

        Args:
            path (str): _description_
        """
        examining_crates = True
        self.crates = {}
        self.instructions = []

        temp_crates = defaultdict(list)
        for line in utils.lines(path):
            if examining_crates:
                if line.startswith(" 1"):
                    # Time to exit "examining crates mode". Eventually we'll convert the indexes to stack numbers.
                    examining_crates = False
                    stack_indices = line
                else:
                    for index, char in enumerate(line):
                        if char.isalpha():
                            temp_crates[index].insert(0, char)
            elif line.startswith("move"):
                self.instructions.append(line)

        # Construct self.crates using the actual stack numbers. The keys in temp_crates represent the n-th character of
        # the stack indices line where the actual stack number is.
        for index, crates in temp_crates.items():
            stack_number = stack_indices[index]
            self.crates[int(stack_number)] = crates

        # Now we run the instructions.
        for command in self.instructions:
            match_groups = re.match(r"move (\d+) from (\d+) to (\d+)", command).groups()
            times, source, target = [int(group) for group in match_groups]
            self.move_crates(times, source, target)

    def move_crates(self, times: int, source: int, target: int):
        """
        Move the end (top-most) item from the 'source' stack and put it at the end of the target stack.

        Args:
            times (int): The number of crates to move - one at a time.
            source (int): Stack number to pop from.
            target (int): Stack number to append to.
        """
        for _ in range(times):
            self.crates[target].append(self.crates[source].pop())

    def get_top_crates(self):
        """
        Return, in order, the topmost item from each stack.
        """
        return [items[-1] for _, items in sorted(self.crates.items())]


class CrateMover9001(CrateMover9000):
    """
    A significantly enhanced model over the CrateMover 9000, the CrateMover 9001 has the ability to move multiple
    crates at the same time while preserving their order.
    """

    def move_crates(self, times: int, source: int, target: int):
        """
        Moves "times" number of crates in one motion.

        Args:
            times (int): The number of crates to move at once. In reality, the CrateMover 9001 only does this once.
            source (int): Stack number to pop from.
            target (int): Stack number to append to.
        """
        staying, being_moved = self.crates[source][:-times], self.crates[source][-times:]
        self.crates[source] = staying
        self.crates[target].extend(being_moved)


def first_star() -> str:
    """
    First star solution.

    Returns:
        str: The letters on top of each stack after processing the moving commands with the CrateMover 9000.
    """
    crates = CrateMover9000("fixtures/day5.txt")
    return "".join(crates.get_top_crates())


def second_star() -> str:
    """
    Second star solution.

    Returns:
        str: The letters on top of each stack after processing the moving commands with the CrateMover 9001.
    """
    crates = CrateMover9001("fixtures/day5.txt")
    return "".join(crates.get_top_crates())


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
