from board import new_board
from solve import solve


def test_solve():
    # TODO: patch vocab to be the below
    # VOCAB = ["beer", "rave", "asia", "yell", "bray", "ease", "evil", "real"]
    pattern = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
    ]
    b = new_board(pattern)

    solved = solve(b)
    print()
    print(solved)
