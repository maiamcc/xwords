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
        """Returns all possible words reachable from the current node."""
        if wds_so_far is None:
            wds_so_far = []
        if letters_so_far is None:
            letters_so_far = ""
        if prefix is None:
            prefix = self.get_parent_letters()

        if self.terminates:
            wds_so_far.append(prefix + letters_so_far)

        for child in list(self.children.values()):
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
        """Given a node, returns a string of its parents (meaning, all of the
            word that has been spelled so far leading up to this node)."""
        if letters_so_far is None:
            letters_so_far = ""
        if self.parent is None:
            return letters_so_far
        else:
            letters_so_far = self.key + letters_so_far
            return self.parent.get_parent_letters(letters_so_far)

    def valid_word(self, word):
        """If Trie contains the given word (i.e. it's a valid word), return True."""
        # I believe this func will work the same given a string or a letter-list.
        # Cuz who needs type safety, amirite?
        current_node = self
        for i, letter in enumerate(word):
            current_node = current_node.children.get(letter)
            if not current_node:
                return False
            if i == (len(word) - 1): # last letter
                return current_node.terminates

    def get_options(self, word):
        """Given an incomplete word that probably contains some blanks, traverse the trie
        and find all possible ways it could be completed."""
        
        # once we're down to only blank characters, we can call get_all_completions on
        # the subtries we've amassed.
        current_node = self
        subnodes = [self] # better name
        for i, char in enumerate(word):
            # import pdb; pdb.set_trace()
            print(i, char)
            if char.isalpha():
                subnodes = [node.children.get(char) for node in subnodes]
                print([node.key for node in subnodes if node is not None])
            else:
                if any([char.isalpha() for char in word[i:]]):
                    # then this is a blank but there are more letters to come,
                    # so we can't return yet
                    print("found a blank")
                    subnodes = flatten([node.children.values() for node in subnodes])
                    print([node.key for node in subnodes if node is not None])
                else: 
                    # then we can return
                    # TODO: CONTROL FOR LENGTH!!!
                    all_completions = flatten(node.get_all_completions() for node in subnodes)
                    return [wd for wd in all_completions if len(wd) == len(word)]
            if not any(subnodes):
                print("whoops, no valid entries")
                return None

def make():
    """A silly utility func. to make a trivial trie for testing. Ooh, alliteration."""
    t = Trie()
    for wd in ["hell", "hello", "help", "helm", "helmet", "heal", "howl", "hole"]:
        t.add_word(wd)
    return t

def flatten(li):
    """Flattens a nested list, removes None entries."""
    # this should work even if list is not nested!
    return [item for sublist in li for item in sublist if item is not None]