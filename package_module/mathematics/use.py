
# This type of import is called Absolute import. Complete path is provided.
from mathematics import basic_math
from mathematics import adavnace_math

# This type of import is called Absolute import. Complete path is provided.
from mathematics.basic_math import add, subtract, divide, multiply
from mathematics.adavnace_math import power

# This type of import is called relative import
from .basic_math import add, subtract, divide, multiply

basic_math.add(4,5)
adavnace_math.power(3,4)