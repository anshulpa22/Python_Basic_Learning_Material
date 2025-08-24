# We can use the absolute path methodology to access the modules
# from mathematics.basic_math import add, subtract, divide, multiply

# from .mathematics import basic_math, adavnace_math, use

# The below is not possible as the system will ask for a absolute path. Thi will work only if we create an init file in the package
from mathematics import add,subtract,multiply,divide,power

print(" this is from app external file")
print(add(2,4))
print(multiply(44,2))
print(power(4,5))