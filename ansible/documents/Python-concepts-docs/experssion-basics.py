print("Hello world!")


print(7.0 / 3.0)  #333333333333333

print(7.0 // 3.0) # 0 -- print only value without remainder as 7.0 is float it gives float division value.

print(7 // 3)    # This is the integer division operator
print(7 % 3)     # This is the remainder or modulus operator

#Example: 16 - 2 * 5 // 3 + 1 

 #--  first *, next //, then , - , +
#Using parentheses, the expression is evaluated as (2*5) first, then (10 // 3), then (16-3), and then (13+1).

16 - 2 * 5 // 3 + 1
16 - 10 // 3 + 1
16 - 3 + 1
13 + 1
14

#()  -->   ** --> //(module)  or  *  --> + or -

print("17") #considered as string
print (12, 23, "hello", 2 ,8)

#What about values like "17" and "3.2"? They look like numbers, but they are in quotation marks like strings.1
print(type("17"))
print(type("3.2"))

print("""This message will span
several lines
of the text.""")
print('This is a string.')
print("""And so is this.""")

print(42500)
print(42,500)

print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)

#Strings in Python can be enclosed in either single quotes (') or double quotes ("), or three of each (''' or """)
print(type('This is a string.'))
print(type("And so is this."))
print(type("""and this."""))
print(type('''and even this...'''))


"""output
Hello world!
2.333333333333333
2.0
2
1
17
12 23 hello 2 8
<class 'str'>
<class 'str'>"""


