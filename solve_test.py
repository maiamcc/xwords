from board import Board, new_board
from solve import solve
from trie import trie_from_words


def four_by_four() -> Board:
    pattern = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
    ]
    return new_board(pattern)


def test_solve():
    vocab = ["beer", "rave", "asia", "yell", "bray", "ease", "evil", "real"]
    wds = trie_from_words(vocab)

    b = four_by_four()

    solved = solve(wds, b)
    assert solved.solved


def test_impossible():
    vocab = ["beep", "boop", "bopp", "blah"]
    wds = trie_from_words(vocab)

    b = four_by_four()

    solved = solve(wds, b)
    assert not solved.solved


def test_try_different_route():
    # B/c solving is currently deterministic, on first pass, `solve` will fill
    # in "abcd" at the top of the board. This creates an impossible board with no
    # possible solution. Ideally, `solve` should realize this, step back up the
    # decision tree, and try again with the first row filled as something different.
    vocab = ["abcd", "cave", "dave", "beer", "rave", "asia", "yell", "bray", "ease", "evil", "real"]
    wds = trie_from_words(vocab)

    b = four_by_four()

    print()
    solved = solve(wds, b)
    assert solved.solved
