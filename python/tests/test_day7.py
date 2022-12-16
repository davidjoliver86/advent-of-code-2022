"""
Test cases for Day 7
"""
from aoc2022 import day7


def test_filesystem():
    """
    Test that the filesystem works as intended.
    """
    filesystem = day7.create_filesystem("tests/fixtures/day7.txt")
    assert filesystem.total_size_report() == {"/": 48381165, "/a": 94853, "/d": 24933642, "/a/e": 584}


def test_file_repr():
    """
    Test that the File's __repr__ works as intended.
    """
    assert repr(day7.File("derp", 1234)) == "File<derp, size=1234>"


def test_directory_repr():
    """
    Test that the Directory's __repr__ works as intended.
    """
    assert repr(day7.Directory("derp")) == "Directory<derp>"


def test_first_star():
    """
    Test first star solution - sum up all folders' sizes whose recursive size is <= 100k.
    """
    assert day7.first_star() == 1243729


def test_second_star():
    """
    Test second star solution - determine the size of the one folder that can be deleted that frees up enough space
    for the update.
    """
    assert day7.second_star() == 4443914
