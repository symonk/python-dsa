"""
Dijkstras Algorithm is search algorithma for detecting the shortest
path between two nodes.

This algorithm is only suitable for problems that can be represented
in a graph-like structure.

To Better understand this algorithm, consider the following scenario:

Person [A] is attempting to cycle from Reykjavik to Belgrade, however
there are various different ways to get there.

1: Reykjavik –> London –> Berlin –> Rome –> Athens –> Moscow –> Belgrade
2: Reykjavik -> Oslo -> -> Beerlin -> Belgrade
... (and so on and so fourth).
"""


class Node:
    """Encapsulation of a Node"""

    def __init__(self) -> None:
        self.distance = float("inf")
        self.parent = None
        self.finished = False


def dijkstras(graph: dict[str, dict[str, int]], source: str) -> None:
    ...
