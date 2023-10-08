import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mypackage.even_odd import is_even

def test_even_number():
    assert is_even(2) == True
    assert is_even(10) == True
    assert is_even(0) == True

def test_odd_number():
    assert is_even(1) == False
    assert is_even(7) == False
    assert is_even(11) == False

def test_negative_number():
    assert is_even(-2) == True
    assert is_even(-5) == False
    assert is_even(-10) == True

def test_decimal_number():
    assert is_even(2.0) == True
    assert is_even(1.5) == False
    assert is_even(3.14) == False