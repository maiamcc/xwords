from copy import deepcopy
from typing import Generator

from board import Board


def solve(b: Board) -> Board:
    """Solve the given board, returning the solved version."""
    for solution in next_solutions(b):  # generator
        maybe_solved = solve(solution)
        if maybe_solved.solved:
            return maybe_solved

    # Didn't solve it -- return the current board (wherever we failed to find
    # a valid next step) -- b.solved = false so recursive calls further up
    # the stack know that we failed.
    return b


def next_solutions(b: Board) -> Generator[Board]:
    """
    Generate all possible solutions for the next word on the given board.

    "Next word": starting from the topmost, leftmost blank square, first
    its across-word, then its down-word.
    """
    # remember to copy instead of modifying in place
    pass
