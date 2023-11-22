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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
