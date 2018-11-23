import pytest

from board import BadValueException, InvalidOpException, WALL_CH, Square, new_board, _board_from_letters, squares_to_chars


def test_square_init():
    with pytest.raises(InvalidOpException):
        _ = Square(False, 'a', 0, 0)


def test_square_set():
    s = Square(True, '', 0, 0)
    s.set('a')
    assert s._val == 'a'

    # auto lowercase
    s.set('B')
    assert s._val == 'b'

    # must be 1 char long
    with pytest.raises(BadValueException):
        s.set('abc')

    # must be alpha
    with pytest.raises(BadValueException):
        s.set('1')

    # can't set val for a non-playable square
    nonplayable = Square(False, '', 0, 0)
    with pytest.raises(InvalidOpException):
        nonplayable.set('a')


def test_square_str():
    empty = Square(True, '', 0, 0)
    assert empty.__str__() == '_'

    blocked = Square(False, '', 0, 0)
    assert blocked.__str__() == WALL_CH

    has_val = Square(True, 'a', 0, 0)
    assert has_val.__str__() == 'a'


def test_new_board():
    pattern = [[True, False], [False, True]]
    b = new_board(pattern)

    for y in range(2):
        for x in range(2):
            s = b.get(x, y)
            assert s._val == ''
            assert s.playable == pattern[y][x]
            assert s.x == x
            assert s.y == y


def test_next_blank():
    pattern = [
        [False, False, True],
        [False, True, False],
        [True, True, True]
    ]
    b = new_board(pattern)
    squ = b.next_blank()
    assert squ.y == 0
    assert squ.x == 2

    b.get(2, 0).set('a')
    squ = b.next_blank()
    assert squ.y == 1
    assert squ.x == 1


def test_next_blank_dne():
    pattern = [
        [False, False],
        [False, False]
    ]
    b = new_board(pattern)
    squ = b.next_blank()
    assert squ is None


def test_wd_down_for_squ():
    letters = [
        ['a', WALL_CH, 'm', WALL_CH, WALL_CH, WALL_CH, WALL_CH],
        ['b', 'h', 'n', WALL_CH, WALL_CH, WALL_CH, WALL_CH],
        ['c', 'i', 'o', WALL_CH, WALL_CH, WALL_CH, WALL_CH],
        ['d', 'j', WALL_CH, WALL_CH, WALL_CH, WALL_CH, WALL_CH],
        ['e', WALL_CH, 'p', WALL_CH, WALL_CH, WALL_CH, WALL_CH],
        ['f', 'k', 'q', WALL_CH, WALL_CH, WALL_CH, WALL_CH],
        ['g', 'l', 'r', WALL_CH, WALL_CH, WALL_CH, WALL_CH],
    ]
    b = _board_from_letters(letters)

    # walls on either side (test from beginning, middle, end squares
    expected = ['h', 'i', 'j']
    to_check = [b.get(1, 1), b.get(1, 2), b.get(1, 3)]
    for s in to_check:
        wd = b.wd_down_for_squ(s)
        assert squares_to_chars(wd) == expected

    # starts at top of board
    expected = ['m', 'n', 'o']
    to_check = [b.get(2, y) for y in range(3)]
    for s in to_check:
        wd = b.wd_down_for_squ(s)
        assert squares_to_chars(wd) == expected

    # ends at bottom of board
    expected = ['p', 'q', 'r']
    to_check = [b.get(2, y) for y in range(4,len(b._squares))]
    for s in to_check:
        wd = b.wd_down_for_squ(s)
        assert squares_to_chars(wd) == expected

    # spans full board
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    to_check = [b.get(0, y) for y in range(len(b._squares))]
    for s in to_check:
        wd = b.wd_down_for_squ(s)
        assert squares_to_chars(wd) == expected

    # called on a wall
    s = b.get(1, 0)
    wd = b.wd_down_for_squ(s)
    assert wd == []
