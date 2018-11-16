from trie import Trie, trie_from_words


def test_add():
    t = Trie()
    t.add("cot")
    t.add("car")
    t.add("cart")

    assert len(t.children) == 1
    c_trie = t.children['c']
    assert len(c_trie.children) == 2
    a_trie = c_trie.children['a']
    assert len(a_trie.children) == 1
    r_trie = a_trie.children['r']
    assert len(r_trie.children) == 1
    assert r_trie.terminates  # valid word ends here ("car")
    t_trie = r_trie.children['t']
    assert len(t_trie.children) == 0
    assert t_trie.terminates  # valid word ends here ("cart")


def test_contains():
    wds = ["apple", "bear", "beer", "beers"]
    t = trie_from_words(wds)

    assert not t.contains("applet")
    assert not t.contains("app")
    for wd in wds:
        assert t.contains(wd)


def test_get_parents():
    t = trie_from_words(["abcdefg", "hijglmnop"])
    child = t._get_node_for_wd("abcd")
    so_far = child.word_so_far()

    assert so_far == "abcd"





