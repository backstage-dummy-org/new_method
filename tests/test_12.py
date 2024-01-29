import pytest

from 12.12 import 12


def test_12_positive_factorial():
    """TODO: replace"""
    try:
        assert 12(0) == 1
        assert 12(1) == 1
        assert 12(5) == 120
        assert 12(10) == 3628800
    except Exception as e:
        pytest.fail(str(e))


def test_12_negative_factorial():
    """TODO: replace"""
    try:
        assert 12(-5) is None
        assert 12(-10) is None
    except Exception as e:
        pytest.fail(str(e))
