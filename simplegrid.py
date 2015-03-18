### Fill a 4x4 grid with valid words ###

import string
import random
import nltk.corpus
LETTERS = string.lowercase
WORDS = nltk.corpus.words.words()

g = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']]

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
fourletter = [word for word in WORDS if len(word) == 4]
row = [0, 0, 0, 0]
grid = [row, row, row, row]

def fill_in_col(grid, x, word):
    for i, row in enumerate(grid):
        row[x] = word[i]

def fill_in_row(grid, i, word):
    grid[i] = [letter for letter in word]
