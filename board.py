#!/usr/bin/env python

from typing import List


class InvalidOpException(Exception): pass
class BadValueException(Exception): pass


class Square:
    def __init__(self, playable: bool, val: str):
        if not playable and val:
            raise InvalidOpException('Square must be playable to have a value')
        self._val = val
        self._playable = playable
        self._x = None
        self._y = None

    def __str__(self) -> str:
        if not self._playable:
            return '■'
        if self.is_blank():
            return '_'
        return self._val

    def set(self, val: str):
        if not self._playable:
            raise InvalidOpException('Square must be playable to set a value')
        if len(val) != 1:
            raise BadValueException(
                'Value to `set` must be a single character (passed {}'.format(val))
        if not val.isalpha():
            raise BadValueException(
                'Value to `set` must be alpha (passed {}'.format(val))
        self._val = val.lower()

    def is_blank(self) -> bool:
        return self._playable and not self._val


def new_square(playable: bool) -> Square:
    return Square(playable, '')


class Board:
    def __init__(self, squares: List[List[Square]]):
        self._squares = squares

    def __str__(self) -> str:
        res = []
        for row in self._squares:
            res.append(' '.join([squ.__str__() for squ in row]))
        return '\n'.join(res)


def new_board(pattern: List[List[bool]]):
    # TODO: validate input (square, all rows same len)
    squares = []
    for row in pattern:
        squares.append([new_square(playable) for playable in row])

    return Board(squares)