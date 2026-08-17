# #Even or Odd — Easy
# # Take an integer from the user and determine whether it's even or odd using % and if/else. Bonus: also identify whether the number is positive, negative, or zero.

# num=int(input("Enter any number : "))

# if(num>0 and num%2==0):
#     print(f"{num} is an even positive number ")
# elif(num<0 and num%2==0):
#     print(f"{num} is an even negative number ")
# elif(num>0 and num%2!=0):
#     print(f"{num} is an odd positive number ")
# elif(num<0 and num%2!=0):
#     print(f"{num} is an odd negative number ")
# else:
#     print("The number is ZERO") 

# # Age & Driving Eligibility — Easy
# # Ask for the user's name and age. Display whether they are eligible to drive based on age >= 18. Add validation so ages below 0 or above 120 are considered invalid.

# name=input("Enter your name :")
# age=int(input("Enter your age :"))

# if(age>=18 and age <=120):
#     print(f"{name } is eligible for the driving test !!!")
# elif(age==0):
#     print("Invalid !!!")
# else:
#     print(f"{name } is not eligible for the driving test !!!")

# Largest of Three Numbers — Medium
# Take three numbers and determine which is the largest using comparison and logical operators. Also handle the case where two or all three numbers are equal.

# num1=int(input("Enter the first number :"))
# num2=int(input("Enter the second number :"))
# num3=int(input("Enter the third number :"))

# if(num1==num2==num3):
#     print("All the numbers are same")
# elif(num1>num2):
#     if(num1>num3):
#         print(num1)
# elif(num2>num3):
#     print(num2)
# else:
#     print(num3)    
 