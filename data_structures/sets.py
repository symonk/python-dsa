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
def difference():
    """Return the difference of one more sets.  Difference
    refers to elements in the initial set, minus those in the others.
    Elements in set A that do not exist in B, ..., n.

    The difference method accepts a single set as an alternative parameter,
    however it implements the `-` operator to enable passing of multiple
    iterables.

    >>> x = set((1,2,3))
    >>> y = set((2,3,4))
    >>> x.difference(y)
    {1}
    >>> x - y
    {1}
    >>> x - y - set((1,))
    set()
    """


@big_o(time_complexity=Complexity.CONSTANT)
def discard():
    """Remove an element from the set if it exists.
    No exception is raised if the element does not exist.
    >>> x = {1,2,3}
    >>> x.discard(4)
    >>> x
    {1, 2, 3}
    >>> x.discard(3)
    >>> x
    {1, 2}

    """


@big_o(time_complexity=Complexity.CONSTANT)
def intersection():
    """Returns a new set that includes element that overlap
    in one or more sets.  Intersection is implemented using
    the & operator and as usual in the operator case can
    handle multiple iterables.

    >>> x = {1,2,3,4,5}
    >>> y = {3,4,5,6,7}
    >>> x & y & set((3,4,5))
    {3, 4, 5}
    >>> x & y & set()
    set()
    >>> x.intersection({3})
    {3}
    """


@big_o(time_complexity=Complexity.LINEAR)
def symmetric_difference():
    """Unlike `set.difference`.  the symmetric difference
    of one more sets is the elements which exist in ANY
    of the sets, but that do not exist in multiple.  Items
    which do not overlap at all.

    Set symmetric difference is implemented via the `^` operator
    and as normal, allows multiple iterables to be provided.

    >>> x = set([99, 88, 77])
    >>> y = set([66, 55, 44])
    >>> z = set([11, 22, 33])
    >>> x ^ y ^ z == {11, 22, 33, 44, 55, 66, 77, 88, 99}
    True
    >>> x.symmetric_difference(z) == {11, 22, 33, 99, 88, 77}
    True
    >>> x ^ set((99, 88, 77))
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
