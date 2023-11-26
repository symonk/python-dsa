"""Default dictionaries are a subclass of dicts, with
an implementation of dunder __missing__ for handling
missing keys.  A factory function provided is calling
for missing values. defaultdict exhibits all the same
performance of its super class `dict`. """


def default_dict() -> None:
    """
    >>> from collections import defaultdict
    >>> def always_100(): return 100
    >>> d = defaultdict(always_100)
    >>> d[1]
    100
    >>> d[2]
    100
    >>> d[2] += 1000
    >>> d[2]
    1100
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
