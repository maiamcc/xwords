import pytest

from board import BadValueException, InvalidOpException, Square, new_board, _board_from_letters


def test_square_init():
    with pytest.raises(InvalidOpException):
        _ = Square(False, 'x', 0, 0)


def test_square_set():
    s = Square(True, '', 0, 0)
    s.set('x')
    assert s._val == 'x'

    # auto lowercase
    s.set('Y')
    assert s._val == 'y'

    # must be 1 char long
    with pytest.raises(BadValueException):
        s.set('abc')

    # must be alpha
    with pytest.raises(BadValueException):
        s.set('1')

    # can't set val for a non-playable square
    nonplayable = Square(False, '', 0, 0)
    with pytest.raises(InvalidOpException):
        nonplayable.set('x')


def test_square_str():
    empty = Square(True, '', 0, 0)
    assert empty.__str__() == '_'

    blocked = Square(False, '', 0, 0)
    assert blocked.__str__() == '■'

    has_val = Square(True, 'x', 0, 0)
    assert has_val.__str__() == 'x'


def test_new_board():
    pattern = [[True, False], [False, True]]
    b = new_board(pattern)

    for x in range(2):
        for y in range(2):
            s = b._squares[x][y]
            assert s._val == ''
            assert s._playable == pattern[x][y]
            assert s._x == x
            assert s._y == y


def test_next_blank():
    pattern = [
        [False, False, True],
        [False, True, False],
        [True, True, True]
    ]
    b = new_board(pattern)
    squ = b.next_blank()
    assert squ._x == 0
    assert squ._y == 2

    b._squares[0][2].set('x')
    squ = b.next_blank()
    assert squ._x == 1
    assert squ._y == 1


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
        ['a', 'a', '_'],
        ['b', 'b', '_'],
        ['c', 'c', '_'],
    ]
    b = _board_from_letters(letters)
    squ = b._squares[1][1]

    print(squ._val)