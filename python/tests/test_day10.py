"""
Test cases for Day 10
"""
from aoc2022 import day10

TEST_CRT_EXPECTED_OUTPUT = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""".strip()

PART_2_EXPECTED_OUTPUT = """
####.#..#.###..####.###....##..##..#....
#....#..#.#..#....#.#..#....#.#..#.#....
###..####.#..#...#..#..#....#.#....#....
#....#..#.###...#...###.....#.#.##.#....
#....#..#.#....#....#....#..#.#..#.#....
####.#..#.#....####.#.....##...###.####.
""".strip()


def test_cpu():
    """
    Test the fundamental behavior of the CPU.
    """
    cpu = day10.CPU()
    cycles = []
    for instruction in (cpu.noop(), cpu.addx(3), cpu.addx(-5)):
        for cycle, reg_x in instruction:
            cycles.append((cycle, reg_x))
    final_reg = cpu.reg_x
    assert (cycles, final_reg) == ([(1, 1), (2, 1), (3, 1), (4, 4), (5, 4)], -1)


def test_snapshot_cycler():
    """
    Tests the behavior of the SnapshotCycler interface and verifies that the signal strength is as expected.
    """
    input_output = day10.SnapshotCycler("tests/fixtures/day10.txt", [20, 60, 100, 140, 180, 220])
    signal_strengths = list(input_output.run())
    assert sum((x[0] * x[1] for x in signal_strengths)) == 13140


def test_crt():
    """
    Tests the behavior of the CRT interface and verifies that the picture rendered is as expected.
    """
    crt = day10.CRT("tests/fixtures/day10.txt")
    crt.run()
    for index, expected in enumerate(TEST_CRT_EXPECTED_OUTPUT.splitlines()):
        actual = "".join(crt.screen[index])
        assert actual == expected


def test_first_star():
    """
    Test first star solution.
    """
    assert day10.first_star() == 12520


def test_second_star():
    """
    Test second star solution.
    """
    crt = day10.second_star()
    for index, expected in enumerate(PART_2_EXPECTED_OUTPUT.splitlines()):
        actual = "".join(crt.screen[index])
        assert actual == expected
