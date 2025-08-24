def add(a,b):
    """
    This is my addition function
    """
    return a + b

def subtract(a, b):
    """
    This is a basic subtract function
    """
    return a - b


def divide(a, b):
    """
    This is a basic divide function
    """
    if b == 0:
        raise ValueError("Change the value of b as it can noty take value 0")
    return a/b

def multiply(a, b):
    """
    This is a basic multiplication function
    """
    return a*b
# the if staement below makes sure that this fuction is executed only when basic_math file is executed and not when we use the functions in
# some different calls
if __name__=="__main__":
     print("this is a print from basic math")
     print(add(2,11))
     print(multiply(2,44))