from board import new_board
from solve import solve
from trie import trie_from_words


def test_solve():
    vocab = ["beer", "rave", "asia", "yell", "bray", "ease", "evil", "real"]
    wds = trie_from_words(vocab)

    pattern = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
    ]
    b = new_board(pattern)

    solved = solve(wds, b)
    assert solved.solved


def test_impossible():
    vocab = ["beep", "boop", "bopp", "blah"]
    wds = trie_from_words(vocab)

    pattern = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
    ]
    b = new_board(pattern)

    solved = solve(wds, b)
    assert not solved.solved
