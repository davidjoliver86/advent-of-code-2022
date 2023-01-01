"""
Day 13: Distress Signal
"""
import json
from typing import List, Optional

from aoc2022 import utils

Packet = int | List[int | List[int]]


def read_packets(path: str) -> List[List[Packet]]:
    """
    Reads the input file and returns a list of signal packet pairings. Empty lines are a sign to start a new "chunk".

    Args:
        path (str): Path of the file.

    Returns:
        List[Packet]: Pairs of packets.
    """
    results = [[]]
    for line in utils.lines(path):
        if not line:
            results.append([])
        else:
            list_obj = json.loads(line)
            results[-1].append(list_obj)
    return results


def read_packets_without_pairs(path: str) -> List[Packet]:
    """
    Reads the input file and returns a list of signal packet pairings. Empty lines are disregarded, as is the notion
    of putting packets in pairs.

    Args:
        path (str): Path of the file.

    Returns:
        List[Packet]: _description_
    """
    return [json.loads(line) for line in utils.lines(path) if line]


def in_order(left: Packet, right: Packet) -> Optional[bool]:
    """
    If both values are integers, the lower integer should come first. If the left integer is lower than the right
    integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are
    not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.

    If both values are lists, compare the first value of each list, then the second value, and so on. If the left list
    runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs
    are not in the right order. If the lists are the same length and no comparison makes a decision about the order,
    continue checking the next part of the input.

    If exactly one value is an integer, convert the integer to a list which contains that integer as its only value,
    then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list
    containing 2); the result is then found by instead comparing [0,0,0] and [2].

    Args:
        left (Packet): Left packet to compare.
        right (Packet): Right packet to compare.

    Returns:
        Optional[bool]: Whether or not the inputs are in the right order. Can return None if more info is needed.
            Anecdotally the entire function should never actually return None though.
    """

    def _compare_ints(left: int, right: int) -> Optional[bool]:
        if left == right:
            return None
        if left < right:
            return True
        return False

    def _compare_lists(left: List[Packet], right: List[Packet]) -> Optional[bool]:
        if len(left) == 0 and len(right) > 0:
            return True

        # Right side ran out, so inputs are not in correct order
        if len(left) > 0 and len(right) == 0:
            return False

        if len(left) == 0 and len(right) == 0:
            return None

        left_val = left[0]
        right_val = right[0]
        left_vs_right = in_order(left_val, right_val)
        if left_vs_right is None:
            return in_order(left[1:], right[1:])
        return left_vs_right

    # Integers
    if isinstance(left, int) and isinstance(right, int):
        return _compare_ints(left, right)

    # Lists
    if isinstance(left, list) and isinstance(right, list):
        return _compare_lists(left, right)

    # Mixed
    if isinstance(left, list) and isinstance(right, int):
        return in_order(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return in_order([left], right)


def merge_sort(_list: List[Packet]) -> List[Packet]:
    """
    Implementation of merge sort for the second star. The merge operation leverages the in_order function defined
    above to enforce ordering.

    Args:
        _list (List[Packet]): The list to sort.

    Returns:
        List[Packet]: The sorted list.
    """
    length = len(_list)
    if len(_list) <= 1:
        return _list
    left = merge_sort(_list[: length // 2])
    right = merge_sort(_list[length // 2 :])
    return merge(left, right)


def merge(left: List[Packet], right: List[Packet]) -> List[Packet]:
    """
    Merges the two lists, then exhausts any remaining elements after one list is exhausted.

    Args:
        left (List[Packet]): Left half to merge.
        right (List[Packet]): Right half to merge.

    Returns:
        List[Packet]: The merged list, which is now sorted.
    """
    ordered = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if in_order(left[left_index], right[right_index]):
            ordered.append(left[left_index])
            left_index += 1
        else:
            ordered.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        ordered.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        ordered.append(right[right_index])
        right_index += 1
    return ordered


def first_star() -> int:
    """
    First star solution.

    Returns:
        int: The sum of the (1-based) indicies of the pairs whose inputs are in order.
    """
    packets = read_packets("fixtures/day13.txt")
    summed_indicies = 0
    for index, pair in enumerate(packets, start=1):
        left, right = pair
        if in_order(left, right):
            summed_indicies += index
    return summed_indicies


def second_star() -> int:
    """
    Second star solution.

    Returns:
        int: The product of the 1-based indices of [[2]] and [[6]] after adding them to the packet list.
    """
    packets = read_packets_without_pairs("fixtures/day13.txt")
    packets.append([[2]])
    packets.append([[6]])
    ordered = merge_sort(packets)
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
