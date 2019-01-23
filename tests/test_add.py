"""
Tests the add() function of the calendar
"""
from calculator import add

def test_two_plus_two():
    """
    if given 2 and 2 as parameters 4 sb returned
    """
    assert add(2, 2) == 4
