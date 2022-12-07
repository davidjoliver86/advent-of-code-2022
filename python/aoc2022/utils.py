"""
General helper utilities
"""
import pathlib


def lines(path: str) -> list[str]:
    """
    Reads a file and returns a list of its lines. Optionally accepts a callable, and if provided,
    applies that callable to all lines.
    Args:
        path (str): Path of the file to read.
        func (Callable, optional): Function to apply to each line (takes one argument). Defaults to None.
        keep_empty (bool): Whether to keep empty lines
    Returns:
        list[Any]: A list of those lines with the callable applied if provided.
    """
    return pathlib.Path(path).read_text("utf-8").splitlines()
