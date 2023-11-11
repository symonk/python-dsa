"""
Heapq is also known as the priority queue algorithm.

Heaps are binary trees for which every parent node, has a value less than
or equal to any of its children.
"""
import heapq


def test_heapify() -> None:
    seq = [9, 4, 5, 7]
    heapq.heapify(seq)
