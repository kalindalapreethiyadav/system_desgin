# system_desgin

Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, 2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use parentheses to make an expression easier to read, as in (minute * 100) / 60: in this case, the parentheses don’t change the result, but they reinforce that the expression in parentheses will be evaluated first.

Exponentiation has the next highest precedence, so 2**1+1 is 3 and not 4, and 3*1**3 is 3 and not 27. Can you explain why?

Multiplication and both division operators have the same precedence, which is higher than addition and subtraction, which also have the same precedence. So 2*3-1 yields 5 rather than 4, and 5-2*2 is 1, not 6.

Operators with the same precedence are evaluated from left-to-right. In algebra we say they are left-associative. So in the expression 6-3+2, the subtraction happens first, yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right to left, the result would have been 6-(3+2), which is 1.


--->Strings in Python can be enclosed in either single quotes (') or double quotes ("), or three of each (''' or """)

# Data Type:
- Python provides several built-in data types to store and manipulate data. 
- Python is a - Dynamically Type Programming language where we are not explicitly mentioning 
the data types definition. 
Below are the data types in the Python:
1. Numeric Types 
2. Sequence Types
3. Mapping Type
4. Set Types
5. Boolean Type
6. Binary Types
7. None Type 


1. Numeric Types:
        a. int: Represents integers, which are whole numbers, positive or negative.
             i. a = 10 # Example of an integer
        b. float: Represents floating-point numbers (decimals).
             i. b = 10.5 # Example of a float
        c. complex: Used for complex numbers, consisting of a real and an imaginary part.
                i. c = 2 + 3j # Example of a complex number
2. Sequence Types
        a. str: Represents strings, which are sequences of Unicode characters.
              i. name = "DevOps Automation" # Example of a string
        b. list: A mutable, ordered collection of items, which can be of any data type.
             i. fruits = ["apple", "banana", "cherry"] # Example of a list
        c. tuple: An immutable, ordered collection of items.
            i. coordinates = (10, 20) # Example of a tuple
3. Dictionary Type
        a. dict: A collection of key-value pairs, where the keys must be unique.
             i. person = {"name": "John", "age": 30} # Example of a dictionary
4. Set Types
        a. set: An unordered collection of unique elements.
            i. numbers = {1, 2, 3, 4} # Example of a set
        b. frozenset: An immutable version of a set.
            i. frozen_numbers = frozenset({1, 2, 3, 4}) # Example of a frozenset 
5. Boolean Type
        a. bool: Represents one of two values: `True` or `False
                i. is_valid = True # Example of a boolea
6. Binary Types
        a. bytes: Immutable sequence of bytes.
            i. byte_data = b"hello" # Example of bytes
        b. bytearray: A mutable sequence of bytes.
            i. byte_array = bytearray(5) # Example of a bytearray with 5 empty byte
7. None Type
        a. NoneType: Represents the absence of a value.
             i. result = None # Example of None type

                    
                    Keywords and Variables:

# Keywords:

Keywords are reserved words in Python that have a predefined meaning and cannot be 
used for anything other than their intended purpose, such as naming variables or functions. 
They are part of the language syntax and serve specific roles like defining functions, control flow, or handling exceptions
 
For example:
- Control flow: if, else, elif, for, while
- Function definition: def, return
- Boolean values: True, False
- Exception handling: try, except, finally, raise

We can see all the list of available keywords using below simple python program.
    import keyword
    print(keyword.kwlist)
Results:
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
    'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# Packages:

A package is a collection of Python modules organized in directories. Each 
package contains an __init__.py file, which signifies that the directory is a Python 
package. Packages help you organize related modules into a hierarchy.

# Creating a Package:

The structure of a package might look like this:
my_package/
    __init__.py # Initializes the package
    module1.py # A module inside the package
    module2.py # Another module

Example of Package:
    my_package/module1.py
    def greet():
    return "Hello from module1"


my_package/module2.py
    def farewell():
    return "Goodbye from module2"

my_package/init.py This file can be empty, or it can define symbols that will be available when you import the package.

Importing a Package:
# main.py
        from my_package import module1, module2

        print(module1.greet()) # Output: Hello from module1
        print(module2.farewell()) # Output: Goodbye from module2

# Installing External Packages:

You can install third-party packages using pip, Python's package manager.
    pip install package_name

For example, installing the popular requests package:
    pip install requests

You can then use it in your program:

        import requests
        response = requests.get("https://api.github.com")
        print(response.status_code


Operators in Python: 

        Operators are symbols that perform operations on variables and values. Python 
    supports various types of operators, categorized based on the type of operations they 
    perform.

Here are the main types of operators in Python:

1. Arithmetic: +, -, *, /, //, %, **
2. Comparison: ==, !=, >, <, >=, <=
3. Logical: and, or, not
4. Assignment: =, +=, -=, *=, /=, //=, %=, **=
5. Bitwise: &, |, ^, ~, <<, >>
6. Identity: is, is not
7. Membership: in, not in



