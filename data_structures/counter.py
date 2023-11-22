"""A Counter is a dictionary subclass where elements are stored as
dictionary keys and their counts as values.  Counts are allowed to be
any integer value including zero, or negative counts.
"""


def initializing_counter() -> None:
    """Counters can be initialized from an iterable.

    >>> from collections import Counter
    >>> t = ('a', 'b', 'c', 'c')
    >>> c1 = Counter(t)
    >>> c2 = Counter({'a': 1, 'b': 1, 'c': 2})
    >>> c1 == c2
    True
    """


def additional_initialization() -> None:
    """
    >>> from collections import Counter
    >>> c1 = Counter("foobar")
    >>> c2 = Counter(f=1, o=2, b=1, a=1, r=1)
    >>> c1 == c2
    True
    """


def counter_missing_items() -> None:
    """When a normal dictionary would raise a `KeyError`, a Counter
    instead returns zero.

    >>> from collections import Counter
    >>> d = dict()
    >>> d['foo']
    Traceback (most recent call last):
        ...
    KeyError: 'foo'
    >>> c = Counter()
    >>> c['foo']
    0
    """


def deleting_from_counter() -> None:
    """Setting a value to 0 in a counter, does not remove it.
    Instead use the builtin `del`.
    >>> from collections import Counter
    >>> c = Counter("foo")
    >>> c["o"] = 0
    >>> c
    Counter({'f': 1, 'o': 0})
    >>> del c["o"]
    >>> c
    Counter({'f': 1})
    """


def counter_elements() -> None:
    """Retrieving an iterator over elements, repeating each for the number of it's
    count can be fetched via `counter.elements()`.

    If elements counts are less than 1, they are ignored by .elements()

    >>> from collections import Counter
    >>> c = Counter("foo")
    >>> for element in c.elements():
    ...     print(element)
    f
    o
    o
    >>> c = Counter("foo")
    >>> c["o"] = 0
    >>> for element in c.elements():
    ...     print(element)
    f
    """


def most_common() -> None:
    """Retrieving a list of tuples for the most common `n` elements
    in the counter.  If counter elements are equal, the returned
    tuples are based on insertion order, this is why in the first example
    even tho `o` and `d` are both 2, `d` is returned as it was encountered
    first.

    If `n` is `None`, all items are returned in order.

    >>> from collections import Counter
    >>> c = Counter("yabbadabbadoo")
    >>> c.most_common(3)
    [('a', 4), ('b', 4), ('d', 2)]
    >>> c.most_common()
    [('a', 4), ('b', 4), ('d', 2), ('o', 2), ('y', 1)]
    """


def subtract() -> None:
    """Subtract the counts in another iterable or mapping from
    the counter.
    >>> from collections import Counter
    >>> c = Counter("foobar")
    >>> t = ("ooa")
    >>> c.subtract(t)
    >>> c == Counter("fbr")
    True
    >>> c = Counter("10101010")
    >>> c.subtract({"1": 5, "0": 10})
    >>> c
    Counter({'1': -1, '0': -6})
    """


def total() -> None:
    """Returns the total sum of all counts.
    >>> from collections import Counter
    >>> c = Counter([0] * 100)
    >>> c.total() == 100
    True
    """


def fromkeys() -> None:
    """The usual `fromkeys` method of dictionaries is not implemented
    for `Counter` objects.
    >>> from collections import Counter
    >>> c = Counter.fromkeys((1,2,3), 100)
    Traceback (most recent call last):
        ...
    NotImplementedError: Counter.fromkeys() is undefined.  Use Counter(iterable) instead.
    """


def update() -> None:
    """Update the counter from an iterable or mapping.  The iterable should just
    be a sequence of elements and rather than replace elements, their counts are
    added.

    >>> from collections import Counter
    >>> c = Counter((1,2,3))
    >>> c.update((3,4,5))
    >>> c == Counter((1, 2, 3, 3, 4, 5))
    True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
