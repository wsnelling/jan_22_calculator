"""
Tests the add() function of the calendar
Note:
It seems that the main purpose of this exercise was to introduce us to the
concept of unit testing using a simple example. It showed us how the
pytest library works and how to use the "assert" function to test a range
of scenarios. We made trivial adjustments to the code at each step of
development in order to demonstrate the step by step nature of applying
test driven development TDD methodology. For example we added each of the
scenario definitions below one by one, and ensured the coding in the
calculator.py file solved each successfully before adding the next test. If
a given test failed we adjusted the coding in thd calculator.py file until
the scenario ran without errors

"""
import pytest
# pytest is a library - you import these before your own libraries.
# pytest has an approx function that will clear up any decimal rounding
# errors that might otherwise emerge - ilustrated in last test below
from calculator import add

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

def test_no_parameters():
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
