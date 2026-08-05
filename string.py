#Stirng : Strings are immutable , sequence of unicode characters used to provide a textual behaviour.
str="vaibhav"
print(str)

#String methods , As string is an immutable datatype there its methods creates a new string based on the parent string and then the methods returns the values.

name ="vaibhav"
print(f"My name is {name}")

nameInCapital= name.upper()
print(nameInCapital)

print(f"My name is {name}".upper())

print(name.lower())
print(name.capitalize())
print(name.title())
print(name.casefold())
print(name.swapcase())

# Whitespace removing methods , used to remove the whitespaces from the string.

str="******Vaibhav*********"

print(str)

newStr=str.strip("*")
print(newStr)

print(str.lstrip("*"))
print(str.rstrip("*"))

# Search and finding methods , 

string="My name is vaibhav and I'm learning python"

print(string.find("vaibhav"))
print(string.find("vaibhava"))
print(string.rfind("vaibhav"))
print(string.index("vaibhav"))
# print(string.index("vaibhav1")) Valueerror
print(string.count("n"))

#Startswith and Endswith.

