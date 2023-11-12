""" Linked lists come in multiple forms, typically
singly linked lists and doubly linked lists.

In the single variant nodes keep a reference to
their next pointer, but its simply one directional.
"""


class Node:
    """Encapsulation of a Linked List Node."""

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, vals: list[int]) -> None:
        self.head = None
        for n in vals:
            node = Node(n)  # noqa
