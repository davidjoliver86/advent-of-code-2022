"""
Day 2: Rock Paper Scissors
"""
from typing import Callable

from aoc2022 import utils

# Constants
OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"
YOU_ROCK = "X"
YOU_PAPER = "Y"
YOU_SCISSORS = "Z"
YOU_MUST_LOSE = "X"
YOU_MUST_DRAW = "Y"
YOU_MUST_WIN = "Z"
SCORE_ROCK = 1
SCORE_PAPER = 2
SCORE_SCISSORS = 3
SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6

# The column in the second star dictates the desired game outcome. Based on that, and the opponent's throw, this
# contains the shape you need to throw to achieve that outcome.

WHAT_TO_PLAY = {
    (OPPONENT_ROCK, YOU_MUST_DRAW): YOU_ROCK,
    (OPPONENT_ROCK, YOU_MUST_LOSE): YOU_SCISSORS,
    (OPPONENT_ROCK, YOU_MUST_WIN): YOU_PAPER,
    (OPPONENT_PAPER, YOU_MUST_DRAW): YOU_PAPER,
    (OPPONENT_PAPER, YOU_MUST_LOSE): YOU_ROCK,
    (OPPONENT_PAPER, YOU_MUST_WIN): YOU_SCISSORS,
    (OPPONENT_SCISSORS, YOU_MUST_DRAW): YOU_SCISSORS,
    (OPPONENT_SCISSORS, YOU_MUST_LOSE): YOU_PAPER,
    (OPPONENT_SCISSORS, YOU_MUST_WIN): YOU_ROCK,
}

OUTCOMES = {
    (OPPONENT_ROCK, YOU_ROCK): SCORE_ROCK + SCORE_DRAW,
    (OPPONENT_ROCK, YOU_PAPER): SCORE_PAPER + SCORE_WIN,
    (OPPONENT_ROCK, YOU_SCISSORS): SCORE_SCISSORS + SCORE_LOSS,
    (OPPONENT_PAPER, YOU_ROCK): SCORE_ROCK + SCORE_LOSS,
    (OPPONENT_PAPER, YOU_PAPER): SCORE_PAPER + SCORE_DRAW,
    (OPPONENT_PAPER, YOU_SCISSORS): SCORE_SCISSORS + SCORE_WIN,
    (OPPONENT_SCISSORS, YOU_ROCK): SCORE_ROCK + SCORE_WIN,
    (OPPONENT_SCISSORS, YOU_PAPER): SCORE_PAPER + SCORE_LOSS,
    (OPPONENT_SCISSORS, YOU_SCISSORS): SCORE_SCISSORS + SCORE_DRAW,
}


def second_column_means_shape(opponent: str, player: str) -> int:
    """
    Play the game according to the first star - where the second column of the strategy guide is what shape to play.

    Args:
        opponent (str): Opponent's shape choice.
        player (str): Your shape choice.

    Returns:
        int: Total "score" for this game.
    """
    return OUTCOMES[(opponent, player)]


def second_column_means_outcome(opponent: str, outcome: str) -> int:
    """
    Play the game according to the second star - where the second column of the strategy guide is the desired game
    outcome you are targeting.

    Args:
        opponent (str): Opponent's shape choice.
        outcome (str): Your desired game outcome.

    Returns:
        int: Total "score" for this game.
    """
    your_throw = WHAT_TO_PLAY[(opponent, outcome)]
    return OUTCOMES[(opponent, your_throw)]


def total_score(path: str, strategy: Callable[[str, str], int]) -> int:
    """
    Play a series of games according to a given strategy function.

    Args:
        path (str): _description_
        strategy (Callable[[str, str], int]): _description_

    Returns:
        int: _description_
    """
    total = 0
    for line in utils.lines(path):
        total += strategy(*line.strip().split(" "))
    return total


def first_star() -> int:
    """
    First star solution. Uses the second_column_means_shape strategy guide.

    Returns:
        int: Total score according to second_column_means_shape strategy.
    """
    return total_score("fixtures/day2.txt", second_column_means_shape)


def second_star() -> int:
    """
    Second star solution. Uses the second_column_means_outcome strategy guide.

    Returns:
        int: Total score according to second_column_means_outcome strategy.
    """
    return total_score("fixtures/day2.txt", second_column_means_outcome)


if __name__ == "__main__":  # pragma: no cover
    print(first_star())
    print(second_star())
