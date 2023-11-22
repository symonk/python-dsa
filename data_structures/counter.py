"""A Counter is a dictionary subclass where elements are stored as
dictionary keys and their counts as values.  Counts are allowed to be
any integer value including zero, or negative counts.
"""


def initialize_counter_from_iterable() -> None:
    """Counters can be initialized from an iterable.

    >>> t = ('a', 'b', 'c', 'c')
    >>> Counter(t)
    Counter(1)

    """


def initialize_counter_from_mapping() -> None:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
