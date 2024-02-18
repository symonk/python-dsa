"""Two pointer is a technique that involves storing two pointers,
often to sequence indexes and iterating through the data.  This often
allows O(n) performance for problems where iterating the sequence multiple
times would otherwise be required."""


def target_indices(seq: list[int], target: int) -> tuple[int, int]:
    """Return the target indexes as a tuple such that
    both indices values in seq add up to the target.
    Return a tuple of negative -1 where no such solution is viable."""
    p0, p1 = 0, len(seq) - 1
    while p0 < p1:
        total = seq[p0] + seq[p1]
        if total == target:
            return (p0, p1)
        if total < target:
            p0 += 1
        else:
            p1 -= 1
    return (-1, -1)
