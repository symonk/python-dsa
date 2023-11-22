from sliding_window import fixed_sized_sliding_window
from sliding_window import dynamically_sized_sliding_window


def test_fixed_size_sliding_window() -> None:
    result = fixed_sized_sliding_window(seq=[1, 12, -5, -6, 50, 3], k=4)
    assert result == 12.75000


def test_dynamic_size_sliding_window() -> None:
    _ = dynamically_sized_sliding_window(seq=[1, 2])
