"""This technique allows us to find the
majority element.  By majority element we
mean the element which appears more than the
average numbers in a given sequence."""


def boyers_moore(seq: list[int]) -> int:
    """Without a hashmap this can achieve O(1) space complexity
    while maintaining the O(n) time complexity.

    :param seq: A sequence of numbers.

    This works on the assumption that there is always one
    majority element."""

    if len(seq) < 2:
        return seq[0]
    ptr0 = 0
    count = 1
    result = seq[0]
    while ptr0 < len(seq):
        if seq[ptr0] == result:
            count += 1
        else:
            count -= 1
        if not count:
            count += 1
            result = seq[ptr0]
        ptr0 += 1
    return result
