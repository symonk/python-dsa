"""Default dictionaries are a subclass of dicts, with
an implementation of dunder __missing__ for handling
missing keys.  A factory function provided is calling
for missing values. defaultdict exhibits all the same
performance of its super class `dict`. """
from collections import defaultdict


def test_default_dict() -> None:
    def always_100() -> int:
        return 100

    d: dict[int, int] = defaultdict(always_100)
    d[1]
    d[2]
    assert d == {1: 100, 2: 100}
