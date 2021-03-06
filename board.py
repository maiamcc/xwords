#!/usr/bin/env python

from copy import deepcopy
from typing import List, Optional

from trie import Trie
from words import is_valid

class InvalidOpException(Exception): pass
class BadValueException(Exception): pass


WALL_CH = '■'

class Square:
    def __init__(self, playable: bool, val: Optional[str], x: int, y: int):
        if not playable and val:
            raise InvalidOpException('Square must be playable to have a value')
        self._val = val
        self.playable = playable

        self.x = x
        self.y = y

    def __str__(self) -> str:
        if not self.playable:
            return WALL_CH
        if self.is_blank():
            return '_'
        return self._val

    def set(self, val: str):
        if not self.playable:
            raise InvalidOpException('Square must be playable to set a value')
        if val is None:
            self._val = None
            return
        if len(val) != 1:
            raise BadValueException(
                'Value to `set` must be a single character (passed {}'.format(val))
        if not val.isalpha():
            raise BadValueException(
                'Value to `set` must be alpha (passed {}'.format(val))
        self._val = val.lower()

    def is_blank(self) -> bool:
        return self.playable and not self._val


def new_square_with_pos(x: int, y: int, playable: bool) -> Square:
    return Square(playable, None, x, y)


def squares_to_chars(squs: List[Square]) -> List[Optional[str]]:
    return [s._val for s in squs]


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
        return self._squares[y][x]

    def next_blank(self) -> Optional[Square]:
        """Get the next (i.e. topmost, leftmost) blank square."""
        for row in self._squares:
            for squ in row:
                if squ.is_blank():
                    return squ
        return None

    def wd_down_for_squ(self, squ: Square) -> List[Square]:
        """Get the down-word that this square is a part of."""
        if not squ.playable:
            return []

        start_y = squ.y  # y index of start of the word
        for y in reversed(range(squ.y)):
            if not self.get(squ.x, y).playable:
                break
            start_y = y

        end_y = squ.y  # y index of end of word (inclusive)
        for y in range(squ.y, len(self._squares)):
            if not self.get(squ.x, y).playable:
                break
            end_y = y

        return [self.get(squ.x, y) for y in range(start_y, end_y+1)]

    def wd_acr_for_squ(self, squ: Square) -> List[Square]:
        """Get the across-word that this square is a part of."""
        if not squ.playable:
            return []

        start_x = squ.x  # x index of start of the word
        for x in reversed(range(squ.x)):
            if not self.get(x, squ.y).playable:
                break
            start_x = x

        end_x = squ.x  # x index of end of word (inclusive)
        for x in range(squ.x, len(self._squares[squ.y])):
            if not self.get(x, squ.y).playable:
                break
            end_x = x

        return [self.get(x, squ.y) for x in range(start_x, end_x+1)]

    def affected_wds(self, squ: Square) -> List[List[Square]]:
        """Get all words that this square is a part of."""
        return [self.wd_acr_for_squ(squ), self.wd_down_for_squ(squ)]

    def next_to_solve(self) -> List[Square]:
        """Get squares representing the next word that needs solving."""

        next_squ = self.next_blank()
        if next_squ is None:
            # No blank squares!
            return []

        across = self.wd_acr_for_squ(next_squ)
        if any([squ.is_blank() for squ in across]):
            return across
        return self.wd_down_for_squ(next_squ)

    def new_with_fill(self, squs: List[Square], word: str):
        copied = deepcopy(self)
        for i, squ in enumerate(squs):
            copied.get(squ.x, squ.y).set(word[i])
        return copied

    def validate(self, wds: Trie, squs: List[Square]) -> bool:
        """
        For each given square, ensure that the across and down words it belongs
        to are either valid (i.e. a word in the dict.) or potentially valid (there
        are OPTIONS in the dict. that can complete it).
        """
        for squ in squs:
            # TODO: redundant validation here, can make a set of already-validated wds
            acr = self.wd_acr_for_squ(squ)
            acr_valid = is_valid(wds, squares_to_chars(acr))
            if not acr_valid:
                return False
            down = self.wd_down_for_squ(squ)
            down_valid = is_valid(wds, squares_to_chars(down))
            if not down_valid:
                return False
        return True


def new_board(pattern: List[List[bool]]):
    # TODO: validate input (square, all rows same len)
    squares = []
    for y, row in enumerate(pattern):
        srow = []
        for x, playable in enumerate(row):
            srow.append(new_square_with_pos(x, y, playable))
        squares.append(srow)

    return Board(squares)


def _board_from_letters(letters: List[List[Optional[str]]]) -> Board:
    # NOTE: Use ■ to signify unplayable square.
    squares = []
    for y, row in enumerate(letters):
        srow = []
        for x, letter in enumerate(row):
            squ = new_square_with_pos(x, y, letter != WALL_CH)
            if letter != WALL_CH:
                squ.set(letter)
            srow.append(squ)
        squares.append(srow)

    return Board(squares)
