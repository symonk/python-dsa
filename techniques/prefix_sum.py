"""The prefix sum technique is useful for generating a running sum of
a given sequence, often the sum or product of said sequence."""


def prefix_prod(seq: list[int]) -> list[int]:
    """Compute and return the product of the sequence."""
    store = [0] * len(seq)
    store[0] = seq[0]
    for i in range(1, len(store)):
        store[i] = store[i - 1] * seq[i]
    return store
