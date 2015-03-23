### Fill a 4x4 grid with valid words ###

from collections import namedtuple
from copy import copy
import string
import re
import random
import nltk.corpus
LETTERS = string.lowercase
WORDS = nltk.corpus.words.words()
# BLANK = "_" # character representing a blank
AffectedEntry = namedtuple("AffectedEntry", ["wd_so_far", "old_wd_index", "new_wd_index"])
# ^ represents the effect that adding a new word would have on a single entry. E.g.,
    # the word far is "B E _ _", the letter that would be changed in that word is the
    # letter at index 3 (old_wd_index = 3), the letter that would go there from the new
    # word would be the first letter (new_wd_index = 0).
samplegrid = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']]

# Print a 4x4 grid.
def print_grid(grid):
    """'Grid' represent a 4x4 grid (list of lists)."""
    print "\n"
    for row in grid:
        print "\t", "   ".join(row), "\n"

# Fill a 4x4 grid at random.
def random_grid():
    grid = []
    for y in range(4):
        row = []
        for x in range(4):
            row.append(random.choice(LETTERS))
        grid.append(row)
    return grid

# Check that all things in a 4x4 grid are valid words.
# ...

# Fill in acr, dwn, acr, down, acr, down
global fourletter
fourletter = [word for word in WORDS if len(word) == 4]

row = ["_", "_", "_", "_"]
g = [copy(row), copy(row), copy(row), copy(row)]

def get_row(grid, y):
    """Given the y value (index of the row), return row contents."""
    return grid[y]

def get_col(grid, x):
    """Given the x value (index of the column), return column contents."""
    return [row[x] for row in grid]

def get_entries_affected(grid, index, dir):
    """Returns a list of AffectedEntries from playing a word in a certain place/direction. `Dir`
        should be `acr` or `dwn` -- indicates the direction the new word is going to be played in.
        `Index` is the x or y at which the world will be played(should have a better name)."""
    results = []
    if dir == "acr":
        for i in xrange(4):
            results.append(AffectedEntry(get_col(grid, i), index, i))
    elif dir == "dwn":
        for j in xrange(4):
            results.append(AffectedEntry(get_row(grid, j), index, j))
    else:
        raise Exception("Womp womp, unrecognized direction. Try 'acr' or 'dwn'.")

    return results

def valid_wd_or_options_exist(xword_entry):
    # or should i return the option list?
    if str(xword_entry).lower() in fourletter:
        return True
    else:
        pattern = "".join(xword_entry).replace("_", ".")
        options = [word for word in fourletter if re.match(pattern, word)]
        print xword_entry, "--", options
        return bool(options)

def check_fill_in(affected_list, new_word):
    for affected in affected_list:
        wd_to_check = affected.wd_so_far
        wd_to_check[affected.old_wd_index] = new_word[affected.new_wd_index]
        if not valid_wd_or_options_exist(wd_to_check):
            print "Whoops, at least one word isn't valid or has no options:", "".join(wd_to_check)
            return False
    return True

def fill_in_row(grid, y, word):
    """Place the given word in the row at index y."""
    grid[y] = [letter for letter in word]

def fill_in_col(grid, x, word):
    """Place the given word in the column at index x."""
    for i, row in enumerate(grid):
        row[x] = word[i]