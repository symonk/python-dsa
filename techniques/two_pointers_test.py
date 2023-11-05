from two_pointers import target_indices


def test_target_indices():
    assert target_indices([1, 2, 3, 4, 5], 3) == (0, 1)
    assert target_indices([1, 3, 5, 7, 9], 99) == (-1, -1)
