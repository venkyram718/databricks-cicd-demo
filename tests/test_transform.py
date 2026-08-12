import pytest
import sys
sys.path.insert(0, 'notebooks')
from transform_data import calculate_revenue

def test_normal():
    assert calculate_revenue(10.0, 100) == 1000.0

def test_zero():
    assert calculate_revenue(0, 100) == 0.0

def test_negative_raises():
    with pytest.raises(ValueError):
        calculate_revenue(-1, 100)
