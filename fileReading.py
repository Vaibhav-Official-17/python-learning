# File Handling.

file=open("E:/AI-Engineering Data/Python/Codes/python basics/PyLearn/utilities","r")
data=file.read()
print(data)
file.close()

with open("E:/AI-Engineering Data/Python/Codes/python basics/PyLearn/utilities/data.txt","r") as f:
    data=f.read()
    print(data)

# Read VS ReadLine VS readLines

with open("E:/AI-Engineering Data/Python/Codes/python basics/PyLearn/utilities/data.txt","r") as f:
    # print(f.readline())
    readLines=f.readlines()


# print(read)
# print(readLine)
for line in range(len(readLines)):
    if(readLines[line].strip()=="vaibhav"):
        print("Yes")
    else:
        print("No")


