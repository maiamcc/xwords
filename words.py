from typing import List, Optional

import trie


def opts_for_chars(wds: trie.Trie, chars: List[Optional[str]]) -> List[str]:  # Generator[str]:
    # e.g. chars = ["C", None, "T"]
    return wds.get_options(chars)


def is_valid(wds: trie.Trie, chars: List[Optional[str]]) -> bool:
    """Returns True if the chars+blanks form a valid word, or if there exist
    valid word(s) that could complete it."""
    # TODO: This doesn't need to get ALL options, we only care that there's at least one.
    opts = wds.get_options(chars)
    return bool(opts)


def clean(wd: str) -> str:
    """
    Reduce the word to alpha characters (i.e. remove any special chars, whitespace etc.)
    """
    return "".join([ch.lower() for ch in wd if ch.isalpha()])