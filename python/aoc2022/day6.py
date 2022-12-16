"""
Day 6: Tuning Trouble
"""
import pathlib


def find_start_marker(lookup: str, packet_size: int) -> int:
    """
    In the lookup string, find the index of the character immediately after the marker. The marker is the character
    immediately following the set of characters packet_size long in which all the characters in the packet are unique.

    Args:
        lookup (str): The string in which to find the start marker.
        packet_size (int): The number of characters in the "packet". All of these characters should be different.

    Returns:
        int: The character number after which the first marker is encountered.
    """
    for index, _ in enumerate(lookup):
        packet = lookup[index : index + packet_size]
        # If all characters are different, then the set of those characters should be equal to the packet size.
        if len(packet) == packet_size and len(set(packet)) == packet_size:
            return index + packet_size
    return None


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: <DESCRIPTION>
    """
    return find_start_marker(pathlib.Path("fixtures/day6.txt").read_text("utf-8"), 4)


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: <DESCRIPTION>
    """
    return find_start_marker(pathlib.Path("fixtures/day6.txt").read_text("utf-8"), 14)


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
