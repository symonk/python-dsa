from dataclasses import dataclass


@dataclass
class Complexity:
    # Complexity remains the same regardless of the input size.
    CONSTANT: str = "O(1)"
    # A complexity where time grows inline with the input size.
    LINEAR: str = "O(n)"
