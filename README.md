# system_desgin

Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, 2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use parentheses to make an expression easier to read, as in (minute * 100) / 60: in this case, the parentheses don’t change the result, but they reinforce that the expression in parentheses will be evaluated first.

Exponentiation has the next highest precedence, so 2**1+1 is 3 and not 4, and 3*1**3 is 3 and not 27. Can you explain why?

Multiplication and both division operators have the same precedence, which is higher than addition and subtraction, which also have the same precedence. So 2*3-1 yields 5 rather than 4, and 5-2*2 is 1, not 6.

Operators with the same precedence are evaluated from left-to-right. In algebra we say they are left-associative. So in the expression 6-3+2, the subtraction happens first, yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right to left, the result would have been 6-(3+2), which is 1.


--->Strings in Python can be enclosed in either single quotes (') or double quotes ("), or three of each (''' or """)

Data Type:
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


1. Numeric Types
    1. int (Integer)
        Whole numbers, positive or negative, without decimals.
        Example: x = 10, y = -3
    2. float (Floating Point)
        Numbers with a decimal point or in exponential (scientific) notation.
        Example: x = 3.14, y = -0.001, z = 2e3 (which is 2000.0)
    3. complex (Complex Numbers)
        Numbers with a real and imaginary part.
        Written as a + bj, where j is the imaginary unit.
        Example: x = 2 + 3j