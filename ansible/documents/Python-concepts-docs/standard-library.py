import math
import os
import json

# import another module inside current module
import my_module

print(math.sqrt(16)) # Output: 4.

print(my_module.sum(2))
def sum(i):
    return i*2


def greet(name):
    print(f"greeting function {name}!")
    

greet("preethi")
print(sum(2))


