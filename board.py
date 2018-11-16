#!/usr/bin/env python

from typing import List


class InvalidOpException(Exception): pass
class BadValueException(Exception): pass


class Square:
    def __init__(self, playable: bool, val: str, x: int, y: int):
        if not playable and val:
            raise InvalidOpException('Square must be playable to have a value')
        self._val = val
        self._playable = playable

        # idk if squares need to know their own pos...
        self._x = x
        self._y = y

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


def new_square_at_pos(x: int, y: int, playable: bool) -> Square:
    return Square(playable, '', x, y)


class Board:
    def __init__(self, squares: List[List[Square]]):
        self._squares = squares
        self.solved = False

    def __str__(self) -> str:
        res = []
        for row in self._squares:
            res.append(' '.join([squ.__str__() for squ in row]))
        return '\n'.join(res)

    def get(self, x: int, y: int) -> Square:
        return self._squares[x][y]

    def next_blank(self) -> Square:
        """Get the next (i.e. topmost, leftmost) blank square."""
        for row in self._squares:
            for squ in row:
                if squ.is_blank():
                    return squ
        return None

    def wd_down_for_squ(self, squ: Square) -> List[Square]:
        """Get the down-word that this square is a part of."""
        # Step up/down until hitting walls/falling off board
        pass

    def wd_acr_for_squ(self, squ: Square) -> List[Square]:
        """Get the across-word that this square is a part of."""
        # Step L/R until hitting walls/falling off board
        pass


def new_board(pattern: List[List[bool]]):
    # TODO: validate input (square, all rows same len)
    squares = []
    for i, row in enumerate(pattern):
        srow = []
        for j, playable in enumerate(row):
            srow.append(new_square_at_pos(i, j, playable))
        squares.append(srow)

    return Board(squares)


def _board_from_letters(letters: List[List[str]]) -> Board:
    # NOTE: Use underscore to signify unplayable square.
    squares = []
    for i, row in enumerate(letters):
        srow = []
        for j, letter in enumerate(row):
            squ = new_square_at_pos(i, j, letter != '_')
            if letter != '_':
                squ.set(letter)
            srow.append(squ)
        squares.append(srow)

    return Board(squares)