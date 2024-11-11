"""Short definition of my module.

This module provides:
- add: a function to add two numbers.
"""

from python_template_uv_example import __version__


def add(a: int, b: int) -> int:
    """Adds two positive numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        sum: The sum of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a + b


def main() -> None:
    print(f"Running python_template_uv_example version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
