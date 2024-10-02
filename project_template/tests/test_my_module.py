"""Tests for the {{python_name}}.my_module"""

import pytest

# from {{python_name}}.my_module import my_function


def test_dummy():
    assert True


def test_my_function():
    # The my_function is not imported, so the expected result is a NameError
    with pytest.raises(NameError):
        assert my_function() == "my_output"

