from typing import List, Generator

import board
import trie

# TODO: nltk
VOCAB = ["hell", "hello", "help", "helm", "helmet", "heal", "howl", "hole"]

WORDS = trie.trie_from_words(VOCAB)


def opts_for_squares(squs: List[board.Square]) -> List[str]:  # Generator[str]:
    chars = board.squares_to_chars(squs)  # ["C", None, "T"]
    return WORDS.get_options(chars)


