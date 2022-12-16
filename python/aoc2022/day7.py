"""
Day 7: No Space Left On Device
"""
from typing import Optional, Self

from aoc2022 import utils


class File:
    """
    Files represent an object in the filesystem with a name and a size.
    """

    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f"File<{self.name}, size={self.size}>"

    def total_size(self) -> int:
        """
        For polymorphism purposes, this just returns the file's size.

        Returns:
            int: Size of this file.
        """
        return self.size


class Directory:
    """
    Directories represent an object in the filesystem that contains either files or other directories.
    """

    def __init__(self, name: str, parent: Optional[Self] = None):
        self.name = name
        self.contents = []
        self.parent = parent

    def __repr__(self):
        return f"Directory<{self.name}>"

    @property
    def full_path(self) -> str:
        """
        Returns a full Unix-style path of this folder, taking into consideration its parents recursively.

        Returns:
            str: The full path of this directory.
        """
        if self.parent is None:
            return self.name
        return "/".join((self.parent.full_path, self.name)).replace("//", "/")

    def add(self, entity: Self | File):
        """
        Adds a file or folder to this directory.

        Args:
            entity (Self | File): The directory or folder to add.
        """
        self.contents.append(entity)

    def total_size(self) -> int:
        """
        Sums up the sizes of all files in this folder, recursively going into any directories beneath.

        Returns:
            int: Total size of all files in this folder.
        """
        total = 0
        for entity in self.contents:
            total += entity.total_size()
        return total

    def total_size_report(self) -> dict[str, int]:
        """
        Computes total_size() across all folders recursively, then returns a report of all folders and their sizes.

        Returns:
            dict[str, int]: A dictionary of folders and their total sizes.
        """
        dirs = [self]
        report = {}
        while dirs:
            current = dirs.pop(0)
            report[current.full_path] = current.total_size()
            for entity in current.contents:
                if isinstance(entity, Directory):
                    dirs.append(entity)
        return report


def create_filesystem(path: str) -> Directory:
    """
    Reads in a text file of commands, then returns a file system according to the files and directories built from
    those commands.

    Args:
        path (str): Text file containing directory traversal and observation commands.

    Returns:
        Directory: The root file system built from the observations.
    """
    filesystem = Directory("/")
    cwd = None
    for line in utils.lines(path):
        if line.startswith("$ cd"):
            path = line.split()[2]
            if path == "/":
                cwd = filesystem
            elif path == "..":
                cwd = cwd.parent
            else:
                for entity in cwd.contents:
                    if entity.name == path and isinstance(entity, Directory):
                        cwd = entity
                        break
        # Directory
        elif line.startswith("dir"):
            name = line.split()[1]
            cwd.add(Directory(name, parent=cwd))
        # File
        elif line.split()[0].isdigit():
            size, name = line.split()
            cwd.add(File(name, int(size)))
    return filesystem


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The sum of all folders' sizes whose recursive size is <= 100k.
    """
    filesystem = create_filesystem("fixtures/day7.txt")
    folders_100k_or_less = {folder: size for folder, size in filesystem.total_size_report().items() if size <= 100000}
    return sum(folders_100k_or_less.values())


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: The size of the one folder that can be deleted that frees up enough space for the update.
    """
    filesystem = create_filesystem("fixtures/day7.txt")
    report = filesystem.total_size_report()
    space_available = 70_000_000 - report["/"]
    update_needs = 30_000_000 - space_available
    candidate_size = report["/"]
    for size in report.values():
        if candidate_size > size > update_needs:
            candidate_size = size
    return candidate_size


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
