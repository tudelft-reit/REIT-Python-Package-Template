"""Short definition of my module.

This module provides:
- add: a function to add two numbers.
"""

from {{ python_name }} import __version__


def add(a: int, b: int) -> int:
    """Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        sum: The sum of the two numbers.

    Raises:
        ValueError: If either a or b is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        msg = "Both arguments must be integers"
        raise ValueError(msg)
    return a + b


def main() -> None:
    print(f"Running {{ python_name }} version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
