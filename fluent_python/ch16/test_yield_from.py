# coding :utf-8
def gen1():
    for c in "AB":
        yield c
    for i in range(1, 3):
        yield i


def gen2():
    yield from "AB"
    yield from range(1, 3)


def chainit(*iterables):
    for it in iterables:
        yield from it


def test_gen():
    assert list(gen1()) == ["A", "B", 1, 2]
    assert list(gen2()) == ["A", "B", 1, 2]
    assert list(chainit("AB", (1, 2))) == ["A", "B", 1, 2]

