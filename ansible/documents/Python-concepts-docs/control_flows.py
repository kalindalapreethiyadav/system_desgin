#############################################################
'''Control Flow: if, elif, else
loops (for, while) 

Asks the user for their name and marks (out of 100).
Prints a message with their name and grade:
90 and above → Grade A
75–89 → Grade B
50–74 → Grade C
Below 50 → Grade F '''
############################################################

name = input("enter name of student: ")
marks = int(input("Enter marks of student out of 100: "))
temperature = float(input("Enter the temperature in Celsius: "))


print(f"Name od the student is: {name} and Marks: {marks}")

if marks >= 90:
    print("Grade A")
elif 75 < marks > 89:
    print("Grade B")
elif 74 < marks >= 50:
    print( "Grade C")
else:
    print("Grade F")

    
'''
1. for Loop
    ✅ Used to iterate over a sequence (like a list, string, or range).
    📌 Example: Print numbers from 1 to 5 '''



