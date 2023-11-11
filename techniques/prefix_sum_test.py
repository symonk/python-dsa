from prefix_sum import prefix_prod


def test_prefix_prod() -> None:
    x = [25, 4, 5]
    assert prefix_prod(x) == [25, 100, 500]
