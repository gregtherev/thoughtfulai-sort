import pytest
from main import sort

def test_standard():
    assert sort(10, 10, 10, 19) == "STANDARD"

def test_heavy():
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_bulky_by_dimension():
    assert sort(10, 1, 150, 10) == "SPECIAL"

def test_bulky_by_volume():
    assert sort(100, 100, 100, 10) == "SPECIAL"

def test_heavy_and_bulky_by_dimension():
    assert sort(10, 10, 150, 20) == "REJECTED"

def test_heavy_and_bulky_by_volume():
    assert sort(100, 100, 100, 25) == "REJECTED"

def test_numeric_string_input():
    assert sort("10.0", 10, 100, "10") == "STANDARD"

def test_non_numeric_string_input():
    with pytest.raises(ValueError):
        sort("ten", 10, 10, 10)

def test_negative_input():
    with pytest.raises(ValueError):
        sort(10, -10, 10, 10)

def test_negative_numeric_string_input():
    with pytest.raises(ValueError):
        sort(10, 10, "-10", 10)
