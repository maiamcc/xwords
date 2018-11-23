import pytest

from board import BadValueException, InvalidOpException, Square, new_board, _board_from_letters, squares_to_chars


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
    assert blocked.__str__() == '■'

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
        ['a', 'd', '_'],
        ['b', 'e', '_'],
        ['c', 'f', '_'],
    ]
    b = _board_from_letters(letters)
    squ = b.get(1, 1)

    print(squ._val)
