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


print("Name od the student is: %s and Marks: %s", name,marks)

if marks >= 90:
    print("Grade A")
elif (marks < 89) && (marks > 75):
    print "Grade B"
elif marks < 74 && marks > 50:
    print( "Grade C")
else:
    print("Grade F")
