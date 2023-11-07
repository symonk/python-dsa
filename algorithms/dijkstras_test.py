from dijkstras import dijkstras


def test_dijkstras_shortest_path():
    graph = {
        "s": {"a": 8, "b": 4},
        "a": {"b": 4},
        "b": {"a": 3, "c": 2, "d": 5},
        "c": {"d": 2},
        "d": {},
    }
    assert dijkstras(graph, "s")
