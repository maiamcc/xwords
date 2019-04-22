#!/usr/bin/env python

import nltk
from nltk.corpus import wordnet as wn

from board import new_board
from solve import solve
from trie import trie_from_words
from words import clean


def all_four_letter_words():
    try:
        all_words = wn.words()
        print("have wordnet, all is well")
    except LookupError:
        print("don't have wordnet, downloading")
        nltk.download('wordnet')
        all_words = wn.words()
    return [clean(wd) for wd in all_words if len(clean(wd)) == 4]


def main():
    vocab = all_four_letter_words()
    wds = trie_from_words(vocab)

    pattern = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
    ]
    b = new_board(pattern)

    solved = solve(wds, b)
    if not solved.solved:
        raise Exception("Could not solve board:\n{}".format(str(solved)))

    print("SOLVED BOARD!")
    print()
    print(solved)


if __name__ == "__main__":
    main()