from board import new_board
from solve import solve


def test_solve():
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
