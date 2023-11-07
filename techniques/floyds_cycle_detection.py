"""The Rabbit and Hare technique is useful for detecting cycles.
It is also known as Floyds Cycle Detection Algorithm.

The technique is simple, using two pointers move one twice as
fast as the other, if they ever point to the same place, a
cycle has been detected."""
from __future__ import annotations
import typing


class Node:
    """A Simple Node."""

    def __init__(self, value: typing.Any) -> None:
        self.value = value
        self.next: typing.Self | None = None


def floyds_detection(head: Node | None) -> bool:
    """Detect a cycle in the linked list."""
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next  # type: ignore [assignment]
        fast = fast.next.next
        if slow is fast:
            return True
    return False
