from typing import List  # , Generator

from board import Board, squares_to_chars
from trie import Trie
from words import opts_for_chars


def solve(wds: Trie, b: Board) -> Board:
    """Solve the given board, returning the solved version."""
    for solution in next_solutions(wds, b):
        if solution.solved:
            return solution

        return solve(wds, solution)

    # Didn't solve it -- return the current board (wherever we failed to find
    # a valid next step) -- b.solved = false so recursive calls further up
    # the stack know that we failed.
    return b


def next_solutions(wds: Trie, b: Board) -> List[Board]:  # Generator[Board]:
    """
    Generate all possible solutions for the next word on the given board.

    "Next word": starting from the topmost, leftmost blank square, first
    its across-word, then its down-word.
    """
    # remember to copy instead of modifying in place

    to_solve = b.next_to_solve()
    if len(to_solve) == 0:
        # board is solved
        b.solved = True
        yield b

    options = opts_for_chars(wds, squares_to_chars(to_solve))
    for opt in options:
        # fill in board and yield if valid
        with_opt = b.new_with_fill(to_solve, opt)
        if with_opt.validate(wds, to_solve):
            yield with_opt