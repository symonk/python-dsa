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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
