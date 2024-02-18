"""Named tuple is a fancier tuple that offers attribute based access
for records or tuple like types.  There are two ways to define a named
tuple, the typing variant is preferred if you want to offer proper type
hinting.  Named tuples are immutable like their tuple equivalents and
that is the main reason why a named tuple may be preferred to using a
dataclass, however with froze=True that is less important.

Use namedtuples when you want an immutable sequence and as such they are
hashable.
"""
from collections import namedtuple
from typing import NamedTuple


def main() -> int:
    record = namedtuple("record", "name age score")

    class Record2(NamedTuple):
        """Largely equivalent to record"""

        name: str
        age: int
        score: int

    t1 = record("john", 18, 100)  # noqa: F841
    t2 = Record2("doe", 30, 75)  # noqa: F841
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
