"""
Script to generate skeleton solution and test files for any given day.
"""

import argparse
import pathlib
import sys

SCRIPT_FOLDER = pathlib.Path(__file__).parent
AOC_FOLDER = SCRIPT_FOLDER.parent / "aoc2022"
TEST_FOLDER = SCRIPT_FOLDER.parent / "tests"


def generate_templates(day: str, title: str, overwrite: bool):
    """
    Creates templates from the given parameters

    Args:
        day (str): Day number (read as a string and strictly used as such).
        title (str): Title of the day's puzzle
        overwrite (bool): Whether to overwrite the files. Defaults to False.
    """
    aoc_template = (pathlib.Path(SCRIPT_FOLDER) / "_solution.py.tpl").read_text()
    aoc_values = aoc_template.format(DAY=day, TITLE=title)
    aoc_path = AOC_FOLDER / f"day{day}.py"
    if not overwrite and aoc_path.exists():
        sys.exit(f"Will overwrite {aoc_path}; pass --overwrite to allow.")
    with aoc_path.open("w") as file:
        file.write(aoc_values)
    print(f"Created answer template for day {day}.")

    test_template = (pathlib.Path(SCRIPT_FOLDER) / "_test.py.tpl").read_text()
    test_values = test_template.format(DAY=day)
    test_path = TEST_FOLDER / f"test_day{day}.py"
    if not overwrite and test_path.exists():
        sys.exit(f"Will overwrite {test_path}; pass --overwrite to allow.")
    with test_path.open("w") as file:
        file.write(test_values)
    print(f"Created test template for day {day}.")


def parse_args() -> argparse.Namespace:
    """
    Parses arguments.

    Returns:
        argparse.Namespace: Argument namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="Day number")
    parser.add_argument("title", help="Daily title")
    parser.add_argument("--overwrite", action="store_true", default=False, help="Overwrite existing files")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    generate_templates(args.day, args.title, args.overwrite)
