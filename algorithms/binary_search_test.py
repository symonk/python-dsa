from binary_search import binary_search


def test_binary_search_in():
    assert binary_search(list(range(10_000)), 500)


def test_binary_search_not_in():
    assert not binary_search([3, 4, 5, 6, 7], 1)
