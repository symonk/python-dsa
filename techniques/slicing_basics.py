# Understanding slicing specifics and range() semantics is vital for
# improving at competitive programming/DSA style puzzles.


def slicing():
    x = [1, 2, 3, 4, 5]
    simple_slice = slice(0, 2)
    assert x[simple_slice] == [1, 2, 3]


def ranging():
    """The vital thing to learn with `range()` is that it is
    INCLUSIVE of the start value, and EXCLUSIVE of the end value."""
    x = range(100, 200)
    assert x[0] == 100
    assert x[-1] == 199
