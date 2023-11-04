"""
This outlined everything to do with sets, specifically in python however a lot of the content
and venn diagrams etc apply to general set theory and provide a generic understanding.

Python sets:
    * Unordered, non indexable collections of distinct, hashable elements.
    * Python offers both the `set` (unhashable) and the `frozenset` (hashable)

Methods:
    ('add',
    'clear',
    'copy',
    'difference',
    'discard',
    'intersection',
    'isdisjoint',
    'issubset',
    'issuperset',
    'pop',
    'remove',
    'union',
    'update')

Documentation: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
from deco import big_o
from const import Complexity


@big_o(time_complexity=Complexity.CONSTANT)
def add():
    """Adds a unique, hashable element into the set.
    >>> x = set()
    >>> x.add(100)
    >>> x
    {100}
    """


@big_o(time_complexity=Complexity.CONSTANT)
def clear():
    """Remove all elements from the set.
    >>> x = set([1,2,3,4,5])
    >>> x.clear()
    >>> x
    set()
    """


@big_o(time_complexity=Complexity.LINEAR)
def copy():
    """Creates a shallow copy of the set.
    >>> x = set((1,2,3))
    >>> y = x.copy()
    >>> x == y
    True
    >>> x is y
    False
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
