"""
A calculator library

Below, I've noted how the calculator.py programming function herein,
evolved through it's various stages before reaching the final code in this
file (following the order of our in-class iterations). -These examples are
also outlined by Marc in the module 2 notes that were presented in SLATE for
this week's class:

1. We started with one simple test in the test_add.py file, as follows:
# tests/tests_add.py
import calculator  # Imports the calculator module (calculator.py)

def test_two_plus_two():
# Asserts that given the parameters 2 and 2, the add
# function should return 4.
    assert calculator.add(2, 2) == 4
Also, we started with this calculator.py file containing no actual add
function - e.g. this file had no coding in it. As a result the test_add
program assertion reported an AttributeError when we ran the test_add program

2. Due to this error we then adjusted the code in this file to include
a simple add function that simply said "pass":
def add():
    pass

3.When we ran test_add with this new calculator code in place we now
got a TypeError because the add definition takes 0 positional arguements
whereas the test_add scenario had 2 numbers to be added together

4.To address this the calculator.py function was adjusted to the
following new definition:
def add(first_number, second_number):
    pass

5.Now when test_add was run we got an AssertionError -the failure being due
to the fact that the value of "pass" in our calculator.py function
is effectively "none", which doesn't equal the sum of the 2 numbers in
the test_add scenario (sb 4 at the time of testing).
SO at this point we've seen illustration of an AttributeError, a
TypeError and an AssertionError.

6. Remembering that the rules of TDD state that on each code adjustment
you try to write the minimum amount of code required to make the test
pass. So next we re-defined calculator.py to:
def add(first_number,second_number):
    return 4
Upon running pytest the above passed successfully.

7. But we only have one test in place and it covers a specific summing
of only 2 values. What happens when we add another test that adds 2
different numbers? So we added another scenario:
def test_five_plus_seven():
    assert calculator.add(5, 7) == 12
and of course this line gave an AssertionError as 5 + 7 doesn't == 4

8. We adjusted calculator.py's function again to the following:
def add(first_number, second_number):
    return first_number + second_number
And test_add now passes successfully again.

9. We next considered other more flexible scenarios - e.g. where no
parameters (e.g. zeros) are used:
def test_no_parameters():
#Asserts that when no parameters are provided, 0 should be returned.
    assert calculator.add() == 0
This gives a TypeError again as add() is missing 2 positional arguements

10. So to solve this we added defaults to our arguements and set them
to zero:
#calculator.py
def add(first_number=0, second_number=0):
return first_number + second_number
And this allows the test to pass

11. So next we considered that our add function should more than 2 numbers,
so we added several tests with more than 2 numbers. The test resulted
in TypeError's for each, as we had only 2 positional arguements
(first_number + second_number) in our calculator.py code

12. To address this last error we change the implementation to loop
over the numbers provided and add them to a running total - this is the
solution contained in the final coding below. This allows the function to
accept any number of parameters - e.g. a variably long list of numbers.
Note that I created a word document from something I found on stack overflow
that explains the use of wildcards and double wildcards in defining python
functions such as the def add(*args) definition below
"""

"""
This code will sum up any list of values.
"""
def add(*args):
    """
    add() Returns the sum of n-parameters
    """
    answer = 0  #This iniitalizes a starting value of zero
    for value in args: #Instructs the code to iterate over each param value
        answer += value  #Adds each parameter value to the total
    return answer
    # note that there is a sum function that does this
    #built into python - we just invented our own
    #you could swap the above out (all below the def)
    #and just put in the following below it
    # sum(args)
