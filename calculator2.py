"""
A calculator library
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

def subtract(*args):
    """" this is the functional docstring for the subtract function """
    answer = 0
    for value in args:
        answer -= value
    return answer

def multiply(*args):
    """" this is the functional docstring for the multiply function """
    if args:
        answer = 1
        for value in args:
            answer *= value
    else:
        answer = 0
    return answer

def divide(*args):
    """ This is the doc string for the divide function"""
    if list(args):
        a_list = list(args)
        answer = a_list[0]
        new_tup = tuple(a_list[1:])
        for value in new_tup:
            answer /= value
            return answer
    else:
        return "ValueError"

    """
    old version of divide - has errors but keeping it as it represents
    a good start

    if list(args):
        try:
            a_list = list(args)
            answer = a_list[0]
            b_list = a_list[1:]
            for value in b_list:
                answer /= value
                return answer
        except ZeroDivisionError:
            return "ZeroDivisionError"
    else:
        return "ValueError"
        """
