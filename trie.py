class Trie():
    def __init__(self, key="", parent=None):
        self.key = key
        self.parent = parent
        self.children = {}
        self.terminates = False

    def add_word(self, wd):
        """Add a word to the trie (creating any necessary sub-tries)."""
        if len(wd) < 1:
            self.terminates = True
        else:
            first_letter = wd[:1]
            rest_of_wd = wd[1:]
            if first_letter in self.children:
                self.children[first_letter].add_word(rest_of_wd)
            else:
                new_trie = Trie(first_letter, self)
                new_trie.add_word(rest_of_wd)
                self.children[first_letter] = new_trie

    def get_all_completions(self, wds_so_far=None, letters_so_far=None, prefix=None):
        """Returns all possible completions of the given word."""
        if wds_so_far is None:
            wds_so_far = []
        if letters_so_far is None:
            letters_so_far = ""
        if prefix is None:
            prefix = self.get_parent_letters()

        if self.terminates:
            wds_so_far.append(prefix + letters_so_far)

        for child in self.children.values():
            child.get_all_completions(wds_so_far, letters_so_far + child.key, prefix)

        return wds_so_far

    def get_sub_trie(self, wd):
        """This... gets the trie that's the endpoint of the given word/prefix/string?
        I guess? Past Maia, what were you trying to do with this function?"""
        if len(wd) < 1:
            return self
        else:
            first_letter = wd[:1]
            rest_of_wd = wd[1:]
            return self.children[first_letter].get_sub_trie(rest_of_wd)

    def get_parent_letters(self, letters_so_far=None):
        """Given a trie, returns a string of its parents (meaning, all of the
            word that has been spelled leading up to this trie)."""
        if letters_so_far is None:
            letters_so_far = ""
        if self.parent is None:
            return letters_so_far
        else:
            letters_so_far = self.key + letters_so_far
            return self.parent.get_parent_letters(letters_so_far)

    def valid_word(self, word):
        """If trie contains the given word (i.e. it's a valid word), return True."""
        # or should this take a list?
        currentNode = self
        for i, letter in enumerate(word):
            currentNode = currentNode.children.get(letter)
            if not currentNode:
                return False
            if i == (len(word) - 1): # last letter
                return currentNode.terminates


def make():
    """A silly utility func. to make a trivial trie for testing. Ooh, alliteration."""
    t = Trie()
    for wd in ["hell", "hello", "help", "helm", "helmet"]:
        t.add_word(wd)
    return t

