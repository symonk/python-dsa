"""
The `range` function is a builtin function that returns an
immutable sequence of numbers.  It can accept an optional
`stop` & `step` argument to dictate the upper bounds and
per iteration value it yields.
"""


def basic_range(start_inclusive: int, end_exclusive: int, step: int = 1) -> list[int]:
    """For consistency with slicing, the range builtin
    returns the start (inclusive) and ends on end-1."""
    return list(range(start_inclusive, end_exclusive, step))
