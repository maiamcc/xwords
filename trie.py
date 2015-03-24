class Trie():
    def __init__(self, key):
        self.key = key
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
                new_trie = Trie(first_letter)
                new_trie.add_word(rest_of_wd)
                self.children[first_letter] = new_trie

    def get_all_completions(self, wds_so_far=None, letters_so_far=None):
        """Returns all possible completions of the given word."""
        if wds_so_far is None:
            wds_so_far = []
        if letters_so_far is None:
            letters_so_far = ""

        letters_so_far += self.key

        if self.terminates:
            wds_so_far.append(letters_so_far)

        for child in self.children.values():
            child.get_all_completions(wds_so_far, letters_so_far)

        return wds_so_far

    def get_sub_trie(self, wd):
        if len(wd) < 1:
            return self
        else:
            first_letter = wd[:1]
            rest_of_wd = wd[1:]
            return self.children[first_letter].get_sub_trie(rest_of_wd)