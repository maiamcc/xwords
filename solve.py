from typing import List  # , Generator

from board import Board
from words import opts_for_squares


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


def next_solutions(b: Board) -> List[Board]:  # Generator[Board]:
    """
    Generate all possible solutions for the next word on the given board.

    "Next word": starting from the topmost, leftmost blank square, first
    its across-word, then its down-word.
    """
    # remember to copy instead of modifying in place

    to_solve = b.next_to_solve()
    if len(to_solve) == 0:
        # board is solved
        yield b

    options = opts_for_squares(to_solve)
    for opt in options:
        # check validity


        # fill in board and yield
        board_with_opt = b.new_with_fill(to_solve, opt)
    pass
