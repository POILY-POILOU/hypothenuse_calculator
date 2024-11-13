import pytest
from hypotenuse.calculator import calculate_hypotenuse

def test_calculate_hypotenuse():
    assert calculate_hypotenuse(3, 4) == 5.0
    assert calculate_hypotenuse(6, 8) == 10.0

def test_calculate_hypotenuse_invalid_input():
    with pytest.raises(ValueError):
        calculate_hypotenuse(-3, 4)
    with pytest.raises(ValueError):
        calculate_hypotenuse(3, -4)
    with pytest.raises(ValueError):
        calculate_hypotenuse(0, 4)
