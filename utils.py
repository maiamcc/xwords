from typing import List, Optional


def isalpha(ch: Optional[str]) -> bool:
    if ch is None:
        return False
    return ch.isalpha()


def flatten(li: List):
    """Flattens a nested list, removes None entries."""
    # this should work even if list is not nested!
    return [item for sublist in li for item in sublist if item is not None]
