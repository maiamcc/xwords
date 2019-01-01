from typing import List, Optional

from utils import flatten, isalpha


class Trie:
    # TODO: enforce fixed-length Trie?
    def __init__(self, key="", parent=None):
        self.key = key
        self.parent = parent
        self.children = {}
        self.terminates = False

    def __str__(self) -> str:
        lns = []
        if not self.key:
            lns = ['ROOT:']

        for k, v in self.children.items():
            lns.append('\t{}'.format(k))
            childlns = v.__str__().split('\n')
            for ln in childlns:
                lns.append('\t{}'.format(ln))

        return '\n'.join(lns)

    def _get_node_for_wd(self, wd: str):
        """Find the node that represents the given word."""
        if len(wd) == 0:
            return self

        next_node = self.children.get(wd[0])
        if not next_node:
            return None

        return next_node._get_node_for_wd(wd[1:])

    def add(self, wd):
        """Add a word to the trie (creating any necessary sub-tries)."""
        if len(wd) < 1:
            self.terminates = True
        else:
            first_letter = wd[:1]
            rest_of_wd = wd[1:]

            if first_letter not in self.children:
                self.children[first_letter] = Trie(first_letter, self)

            self.children[first_letter].add(rest_of_wd)

    def contains(self, wd):
        """Check if `wd` is a valid word that exists in this Trie."""
        # I believe this func will work the same given a string or a letter-list.
        # Cuz who needs type safety, amirite?
        if len(wd) == 0:
            return self.terminates  # is this trie the end of a word?

        next_node = self.children.get(wd[0])
        if not next_node:
            return False

        return next_node.contains(wd[1:])

    def word_so_far(self, letters_so_far=None):
        """Given a node, returns a string of its parents (meaning, all of the
            word that has been spelled so far leading up to this node)."""
        if letters_so_far is None:
            letters_so_far = ""
        if self.parent is None:  # made it to the top
            return letters_so_far
        else:
            letters_so_far = self.key + letters_so_far
            return self.parent.word_so_far(letters_so_far)

    def get_all_completions(self, wds_so_far=None, letters_so_far=None, prefix=None):
        """Returns all possible words reachable from the current node."""
        if wds_so_far is None:
            wds_so_far = []
        if letters_so_far is None:
            letters_so_far = ""
        if prefix is None:
            prefix = self.word_so_far()

        if self.terminates:
            wds_so_far.append(prefix + letters_so_far)

        for child in list(self.children.values()):
            child.get_all_completions(wds_so_far, letters_so_far + child.key, prefix)

        return wds_so_far

    def get_all_completions_of_len(self, length: int) -> List[str]:
        """Returns all possible words of given len reachable from the current node."""
        # TODO: this still traverses all the way down, we don't need to traverse past n letters
        wds = self.get_all_completions()
        return [wd for wd in wds if len(wd) == length]

    def get_options(self, word: List[Optional[str]]) -> List[str]:
        """Given an incomplete word that probably contains some blanks, traverse the trie
        and find all possible ways it could be completed."""

        # ['r', 'u', None, 'h', None, None] --> 'ruthie', 'rushes'

        subnodes = [self]
        for i, char in enumerate(word):
            if isalpha(char):  # we have a letter -- get a specific child
                subnodes = [node.children.get(char) for node in subnodes]
            else:  # found a blank, so keep looking down all children of current node
                if any([isalpha(char) for char in word[i:]]):
                    # then this is a blank but there are more letters to come,
                    # so we can't return yet
                    subnodes = flatten([node.children.values() for node in subnodes])
                else:
                    # then we can return
                    return flatten(node.get_all_completions_of_len(len(word)) for node in subnodes)
            if not any(subnodes):
                return []
        return [node.word_so_far() for node in subnodes if node.terminates]


def trie_from_words(wds: List[str]) -> Trie:
    t = Trie()
    for wd in wds:
        t.add(wd)

    return t

