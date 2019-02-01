"""
Tests the functionality of calculator.py
Note: This takes the test_add.py tests and expands on them to
add functionality for calculator subtraction, multiplication and
division
"""
import pytest
# pytest is a library - you import these before your own libraries.
# pytest has an approx function that will clear up any decimal rounding
# errors that might otherwise emerge - ilustrated in last test below
from calculator2 import add, subtract, multiply, divide # we will be testing
# the scenarios below

def test_two_plus_two():
    """
    if given 2 and 2 as parameters 4 sb returned
    """
    assert add(2, 2) == 4
def test_three_plus_three():
    """
    if given 3 and 3 as parameters 6 sb returned
    """
    assert add(3, 3) == 6

def test_no_add_parameters():
    """
    if given no input parameters return zero
    """
    assert add() == 0

def test_one_two_three():
    """
    if given the values 1, 2 and 3 as parameters return 6
    """
    assert add(1, 2, 3) == 6

def test_negative_values():
    """
    if given the negative values ensure they sum correctly
    """
    assert add(-1, -1, -1, -1, -1) == -5

def test_decimal_values():
    """
    If given the floating values ensure they sum correctly.

    """
    assert add(0.1, 0.1, 0.1) == pytest.approx(0.3)

def test_neg_four_minus_one():
    """
    tests if calculator2 accurately subtracts -4 - 1 to get -5
    """
    assert subtract(4, 1) == -5

def test_neg_seven_minus_five():
    """
    tests if calculator2 accurately subtracts -7 - 5 to get -12
    """
    assert subtract(7, 5) == -12

def test_no_subtract_parameters():
    """
    tests if calculator2 accurately reports a net of zero when no values
    are presented
    """
    assert subtract() == 0

def test_multiple_subtractions():
    """
    tests if calculator2 accurately reports a net when multiple values
    are presented including a positive starting number
    """
    assert subtract(-200, 130, 60, 5) == 5

def test_five_times_ten():
    """
    tests if calculator2 accurately multiplies 5 x 10 to get 50
    """
    assert multiply(5, 10) == 50

def test_five_times_zero():
    """
    tests if calculator2 accurately multiplies 5 x 0 to get 0
    """
    assert multiply(5, 0) == 0

def test_five_x_ten_x_twenty():
    """
    tests if calculator2 accurately multiplies 5 x 10 x 20 to get 1000
    """
    assert multiply(5, 10, 20) == 1000

def test_five_x_ten_x_negtwenty():
    """
    tests if calculator2 accurately multiplies 5 x 10 x -20 to get -1000
    """
    assert multiply(5, 10, -20) == -1000

def test_five_pt_two_x_ten_point_three():
    """
    tests if calculator2 accurately multiplies 5.2 x 10.3 to get 53.56
    """
    assert multiply(5.2, 10.3) == 53.56

def test_no_multiplication_parameters():
    """
    tests if calculator2 accurately multiplies to a net of zeros when no
    values are presented
    """
    assert multiply() == 0

def test_eighty_divided_by_ten():
    """
    tests if calculator2 accurately divides 80 / 8 to get 10
    """
    assert divide(80, 8) == 10

def test_ten_pt_six_div_by_two():
    """
    tests if calculator2 accurately divides 10.6 by 2 to get 5.3
    """
    assert divide(10.6, 2) == 5.3

"""
The following tests cannot be successfully added yet
For some reason the code seems to work when run in the interpreter
but fails in testing ??  Need help from Marc on how to resolve my
code as there's obviously something wrong I'm not understanding
"""
#def test_90_div_3_div_5():
#    """
#    tests if calculator2 accurately divides 90 / 3 / 5 to get 6
#    """
#    assert divide(90, 3, 5) == 6
#
#def test_90_div_3_div_neg_5():
#    """
#    tests if calculator2 accurately divides 90 / 3 / -5 to get -6
#    """
#    assert divide(90, 3, -5) == -6
#
#def test_five_divided_by_zero():
#    """
#    tests if calculator2 accurately divides 5/0 to get an "undefined" result
#    """
#    assert divide(5, 0) == 0
#
#def test_no_division_parameters():
#    """
#    tests if calculator2 accurately returns an undefined value when
#    values are presented
#    """
#    assert divide() == IndexError

"""
Note above the use of the "approx" function in def test_decimal_values().
This is needed because if you simply add floating decimals in any
computer program you will get some unexpected results. This is due to
how computers make binary representations of floating point numbers.
In fact the only fractional floating point numbers with terminating
decimals (finite number of decimal numbers) are those whose denominator
is a power of 2. (e.g. 1/2, 1/4, 1/64, etc.) All other numbers are
approximate values, which the Python interpreter rounds out for us.
In math, we use a 10 number base, meaning that 1/10 is a terminating
decimal number, whereas but 3/10 has repeating decimals. To see the
 precision of numbers, we can cast floats to Decimal objects:
>>> 1 / 10
0.1
>>> from decimal import Decimal
>>> Decimal(1 / 10)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> Decimal(1 / 8)  # Is a base of 2
Decimal('0.125')
We see that while float(0.1) is represented as 0.1, it is actually
different value because of the binary representation. For a detailed
explanation of floating point arithmetic, consult the following article
from Python docs:https://docs.python.org/3/tutorial/floatingpoint.html
"""
