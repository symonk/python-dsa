def binary_search(haystack: list[int], needle: int) -> bool:
    """Iterative binary search.  Detects if a value is in a
    sorted sequence in O(log n) time, avoiding the overhead of
    a linear search.

    :param haystack: The ordered sequence.
    :param needle: The target to find.
    """
    low, high = 0, len(haystack) - 1
    while low <= high:
        mid = (low + high) // 2
        if haystack[mid] == needle:
            return True
        if haystack[mid] < needle:
            low = mid + 1
        else:
            high = mid - 1
    return False
