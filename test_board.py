import pytest

from board import BadValueException, InvalidOpException, Square, new_board


def test_square_init():
    with pytest.raises(InvalidOpException):
        _ = Square(False, 'x')


def test_square_set():
    s = Square(True, '')
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
    nonplayable = Square(False, '')
    with pytest.raises(InvalidOpException):
        nonplayable.set('x')


def test_square_str():
    empty = Square(True, '')
    assert empty.__str__() == '_'

    blocked = Square(False, '')
    assert blocked.__str__() == '■'

    has_val = Square(True, 'x')
    assert has_val.__str__() == 'x'


def test_new_board():
    pattern = [[True, False], [False, True]]
    b = new_board(pattern)

    assert b._squares[0][0]._val == ''
    assert b._squares[0][0]._playable

    assert b._squares[0][1]._val == ''
    assert not b._squares[0][1]._playable

    assert b._squares[1][0]._val == ''
    assert not b._squares[1][0]._playable

    assert b._squares[1][1]._val == ''
    assert b._squares[1][1]._playable

