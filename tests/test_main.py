"""Tests for the python_template_uv_example.main."""

import pytest

from python_template_uv_example.main import add


def test_add__two_integers():
    expected = 5
    result = add(2, 3)
    assert result == expected, f"Expected {expected}, but got {result}."


def test_add__negative_values_raise_value_error():
    with pytest.raises(ValueError, match="Both arguments must be positive"):
        add(-12, -8)


def test_add__zeros():
    expected = 0
    result = add(0, 0)
    assert result == expected, f"Expected {expected}, but got {result}."
