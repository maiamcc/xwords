from trie import Trie


def test_trie():
    t = Trie()
    t.add_word("cat")
    t.add_word("car")
    t.add_word("bat")
    t.add_word("baal the destroyer")

    print(t)
