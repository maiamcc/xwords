from words import clean


def test_clean():
    # Cases in (given, expected) format
    cases = [
        ("hello", "hello"),
        ("hello world", "helloworld"),
        ("__dunder__", "dunder"),
        ("abc123", "abc"),
        ("abc123def", "abcdef"),
        ("CaPiTaLs", "capitals")
    ]

    for c in cases:
        assert clean(c[0]) == c[1]