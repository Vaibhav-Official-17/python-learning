# Project: Student Result System v2

# Create a Python program that:

# Takes the student's full name, roll number, and marks in 5 subjects: English, Maths, Science, Hindi, and Computer.
# Cleans the student's name by removing unnecessary spaces and formatting it properly.
# Validates that the name contains only letters/spaces.
# Validates that the roll number contains only digits.
# Validates that each subject's marks is numeric and between 0 and 100.
# Calculates total marks, average marks, and percentage.
# Displays a clean formatted student report containing all details and results.
# Generates a student ID using the first 3 letters of the student's name in uppercase + roll number.

# Example: Vaibhav, roll 1024 → VAI-1024

# Use only what you've learned so far: variables, data types, input(), print(), type conversion, arithmetic, f-strings, indexing/slicing, and string methods.

name=input("Enter your name :")
rollNumber=input("Enter your roll number :")
hindi=int(input("Enter your marks in hindi :"))
maths=int(input("Enter your marks in maths :"))
english=int(input("Enter your marks in english :"))
science=int(input("Enter your marks in science :"))
cs=int(input("Enter your marks in cs :"))
name=name.strip()
if(name.isdigit()):
    print("Error1")
    exit(1)

if(rollNumber.isalpha() and rollNumber.isdecimal):
    print("Error2")
    exit(1)


if((hindi<0 and hindi>100) or (maths<0 and maths>100) or (english<0 and english>100) or (science<0 and science>100) or (cs<0 and cs>100)):
    print("Error3")
    exit(1)

print(f"ID : {(name[0:3]).upper()+rollNumber}")