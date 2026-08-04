#Coding problems.
# Personal Introduction Generator — Easy
# Ask for name, age, city, and profession. 
# Print a nicely formatted introduction using an f-string. 
# Also calculate and display the user's age next year.

name=input("Enter you name:")
age=int(input("Enter you age:"))
city=input("Enter you city:")
profession=input("Enter you Profession:")

print(f"Name: {name}\n Age :{age}\n City:{city}\n Profession:{profession}")
print(f"Next year your age will be {age +1 }")

# # Basic Calculator — Easy
# # Take two numbers from the user and display their addition, subtraction, multiplication, and division.
# # Example input 20 and 5 should produce 25, 15, 100, 4.0. This practices input() + conversion + arithmetic.

num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)

# Rectangle Calculator — Easy/Medium
# Ask for length and width. Calculate and display area and perimeter. Use meaningful variable names rather than a, b, x.

lenght=int(input("Enter the lenght of the rectangle :"))
width=int(input("Enter the width of the rectangle :"))
area=lenght*width
perimeter=2*(lenght+width)
print(area)
print(perimeter)

# emperature Converter — Medium
# Ask the user for temperature in Celsius and convert it to Fahrenheit using F = (C × 9/5) + 32. Display both temperatures clearly. Use float() so values like 36.5 work.

c=float(input("Enter the temprature in degree celcius :"))

f=(c*(9/5))+32

print(f)

# Bill Splitter — Medium
# Ask for the total bill amount and number of people. Calculate how much each person should pay. Example: ₹1500 among 4 people → ₹375 each. Bonus: format the result to 2 decimal places.

total = float(input("Enter the total bill : "))
split=int(input("Enter the number of people in which bill will be splited : "))

print(total//split)

# Student Result Calculator — Challenge
# Ask for the student's name and marks in 5 subjects. Calculate total_marks, percentage, and average_marks, then print a clean report such as:

hindi=int(input("Enter the marks in hindi :"))
english=int(input("Enter the marks in english :"))
maths=int(input("Enter the marks in maths :"))
science=int(input("Enter the marks in science :"))
cs=int(input("Enter the marks in cs :"))

print(f"Marks yeild = {hindi+english+maths+science+cs}")
print(f"Average Marks = {(hindi+english+maths+science+cs)/5}")
print(f"Marks yeidl = {((hindi+english+maths+science+cs)/500)*100}")