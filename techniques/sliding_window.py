"""The sliding window technique is useful for solving problems
in sequences, typically strings or lists in python in a single
O(n) pass through the sequence.  Other solutions often require
nested loops.  Our window can be fixed or dynamic in nature and
we typically perform an operation each iteration.
"""
import typing

def sliding_window(seq: typing.Sequence[int], target: int) -> tuple[int, int]:
  """Given a sequence of integers, return both the minimum and
  maximum sum of subarrays of the `target` size.
  :param seq: A sequence of (unordered) integers.
  :param target: The subarray size to sum.

  It is guaranteed that seq will be of at least target size.

  This implementation retries both min and max subarrays in a
  linear O(n) time complexity.
  """
  low, high = 0, 0
  runningSum = sum(nums[:target])
  p0 = target
  while p0 < len(seq):
    window = seq[p0:]
    runningSum = runningSum - (nums[p0-1]) + window[-1]
    low = min(low, runningSum)
    high = max(high, runningSum)
    p0 += 1
  return (low, high)
