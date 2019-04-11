from typing import List, Generator, Optional

import trie

# TODO: nltk
# VOCAB = ["hell", "hello", "help", "helm", "helmet", "heal", "howl", "hole"]
VOCAB = ["beer", "rave", "asia", "yell", "bray", "ease", "evil", "real"]

WORDS = trie.trie_from_words(VOCAB)


def opts_for_chars(chars: List[Optional[str]]) -> List[str]:  # Generator[str]:
    # e.g. chars = ["C", None, "T"]
    return WORDS.get_options(chars)


def is_valid(chars: List[Optional[str]]) -> bool:
    """Returns True if the chars+blanks form a valid word, or if there exist
    valid word(s) that could complete it."""
    # TODO: This doesn't need to get ALL options, we only care that there's at least one.
    opts = WORDS.get_options(chars)
    return bool(opts)
