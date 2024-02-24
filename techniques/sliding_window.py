"""The sliding window technique is useful for solving problems
in sequences, typically strings or lists in python in a single
O(n) pass through the sequence.  Other solutions often require
nested loops.  Our window can be fixed or dynamic in nature and
we typically perform an operation each iteration.
"""
import typing


def fixed_sized_sliding_window(seq: typing.Sequence[int], k: int) -> float:
    """You are given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value."""
    window = seq[:k]
    curr = sum(window)
    max_avg = curr / k
    p0 = 1
    while (p0 + k) <= len(seq):
        window = seq[p0 : p0 + k]
        curr += window[-1]
        curr -= seq[p0 - 1]
        max_avg = max(max_avg, curr / k)
        p0 += 1
    return max_avg


def dynamically_sized_sliding_window(s: str) -> int:
    """Finding all subarrays that meet a particular criteria, where
    the fixed size of the subarray is unknown.

    Given a string `s`, find the length of the longest substring without repeating
    characters.

    Summary of technique:
        * create a set for tracking distinct chars
        * initialise a left and right pointer at 0
        * while right is less than the length of the string s
        * if the latest character in the window is in the set, remove it and slide s
        * else, calculate the max and add the right char to the set.
        * move right up
    """
    seen: set[str] = set()
    left = right = highest = 0
    while right < len(s):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        highest = max(highest, right - left + 1)
        right += 1
    return highest
