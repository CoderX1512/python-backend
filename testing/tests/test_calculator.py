import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mypackage.calculator import Calculator

# create an instance of the Calculator class for testing purposes
calculator = Calculator()


# test the add method
def test_addition():
    assert calculator.add(2, 3) == 5
    assert calculator.add(0, 0) == 0
    assert calculator.add(-1, 1) == 0


# test the subtract method
def test_subtraction():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(0, 0) == 0
    assert calculator.sub(-1, -1) == 0


# test the multiply method
def test_multiplication():
    assert calculator.mul(2, 3) == 6
    assert calculator.mul(0, 5) == 0
    assert calculator.mul(-1, 1) == -1


# test the divide method
def test_divide():
    assert calculator.div(6, 3) == 2
    assert calculator.div(0, 5) == 0
    assert calculator.div(-6, 2) == -3


# Test divide method with zero division
def test_divide_by_zero():
    try:
        calculator.div(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
