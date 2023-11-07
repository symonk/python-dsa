from floyds_cycle_detection import floyds_detection
from floyds_cycle_detection import Node


def test_floyds_cycle_detection_none() -> None:
    assert not floyds_detection(None)


def test_floyds_cycle_detection_yes() -> None:
    root, one, two = Node(0), Node(1), Node(2)
    root.next = one
    one.next = two
    assert not floyds_detection(root)


def test_floyds_cycle_detection_no() -> None:
    root = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    root.next = one
    one.next = two
    two.next = three
    three.next = root
    assert floyds_detection(root)
