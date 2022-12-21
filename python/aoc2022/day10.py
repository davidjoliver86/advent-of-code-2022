"""
Day 10: Cathode-Ray Tube
"""
import dataclasses
from typing import Callable, Optional, Tuple

from aoc2022 import utils

State = Tuple[int, int]


@dataclasses.dataclass
class CPU:
    """
    Represents an abstract CPU with a cycle counter and a register.
    """

    cycle: int = 1
    reg_x: int = 1

    def __init__(self):
        self.cycle = 1
        self.reg_x = 1

    def noop(self) -> State:
        """
        Does nothing (except increment the cycle counter)

        Yields:
            Iterator[State]: State of the cycle counter and register during this step.
        """
        yield self.cycle, self.reg_x
        self.cycle += 1

    def addx(self, value: int) -> State:
        """
        Adds a value to the register X.

        Args:
            value (int): The value to add to X.

        Yields:
            Iterator[State]: State of the cycle counter and register during this step.
        """
        yield self.cycle, self.reg_x
        self.cycle += 1
        yield self.cycle, self.reg_x
        self.reg_x += value
        self.cycle += 1


@dataclasses.dataclass
class InterfaceHandler:
    """
    Represents anything that interfaces with the CPU. This may be some sort of input-output device to feed
    instructions to the CPU and make observations as necessary.

    Raises:
        NotImplementedError: If this exact class is instantiated.
    """

    cpu: CPU
    instructions: list[Callable[[Optional[int]], None]]

    def __init__(self, path: str):
        self.cpu = CPU()
        self.instructions = []
        self._parse_instructions(path)

    def _parse_instructions(self, path: str):
        # Parse instructions and prepare execution.
        for line in utils.lines(path):
            if line == "noop":
                self.instructions.append(self.cpu.noop())
            if line.startswith("addx"):
                value = int(line.split()[1])
                self.instructions.append(self.cpu.addx(value))


@dataclasses.dataclass
class SnapshotCycler(InterfaceHandler):
    """
    The SnapshotCycler takes a list of cycle numbers and will fetch the result of the X register *during* execution of
    that particular cycle if it's in the list.
    """

    snapshot_cycles: list[int]

    def __init__(self, path: str, snapshot_cycles: Optional[list[int]] = None):
        super().__init__(path)
        self.snapshot_cycles = snapshot_cycles or []

    def run(self) -> State:
        """
        Runs through the instructions, yielding the current cycle and register values at the given intervals specified
        by the snapshot_cycles parameter.

        Yields:
            Iterator[State]: State of the cycle counter and register during this step.
        """
        # Execute instructions, yielding snapshots of the state as necessary.
        for instruction in self.instructions:
            for cycle, reg_x in instruction:
                if self.snapshot_cycles and cycle == self.snapshot_cycles[0]:
                    yield (cycle, reg_x)
                    self.snapshot_cycles.pop(0)


class CRT(InterfaceHandler):
    """
    The CRT represents a 40x6 monitor. The register at any given point in time represents the middle pixel of a
    three-pixel wide buffered sprite. If the current row of the electron beam matches up with the sprite, draw a
    pixel.
    """

    screen: list[str]

    def __init__(self, path: str):
        super().__init__(path)
        self.screen = [["." for _ in range(40)] for _ in range(6)]

    def run(self):
        """
        Runs through the instructions, painting a pixel on the screen whenever the current column number of the
        electron beam is equal to or one away from the X register.
        """
        for instruction in self.instructions:
            for cycle, reg_x in instruction:
                row = (cycle - 1) // 40
                col = cycle - 1 - (row * 40)
                sprite = (reg_x - 1, reg_x, reg_x + 1)
                if col in sprite:
                    self.screen[row][col] = "#"

    def draw_screen(self):
        """
        Draws the screen according to the contents of self.screen.
        """
        for row in self.screen:
            print("".join(row))


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The product of the combined "signal strengths" taken at specific snapshot intervals.
    """
    input_output = SnapshotCycler("fixtures/day10.txt", [20, 60, 100, 140, 180, 220])
    signal_strengths = list(input_output.run())
    return sum((x[0] * x[1] for x in signal_strengths))


def second_star() -> CRT:
    """
    Second star solution.
    This particular part relies on printing a "picture" onto the terminal. The larger message in this output *is* the
    part 2 answer. For purposes of testing, this function returns the CRT object itself to make assertions against
    its internal "screen" state.

    Returns:
        CRT: The CRT object.
    """
    crt = CRT("fixtures/day10.txt")
    crt.run()
    crt.draw_screen()
    return crt


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
