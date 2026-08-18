
student=(["akash",False],["asmita",False],["vanshika",False],["sikhsha",False],["jyoti",False],["preeti",False],["tanish",False],["harshit",False],)
print(student)
itretor=1
while(itretor==1):
    print("-----------------Attendence system-----------------")
    print("1.Show all students")
    print("2.Mark attendence")
    print("3.Show attendence")
    print("4.Show absent students")
    print("5.Show attendence percentage")
    print("6.Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        for i in range(len(student)):
            print(student[i][0])
    elif(choice==2):
        print("Enter 'P' for present and 'A' for absent")
        for i in range(len(student)):
            attendence=input(f"{student[i][0]}: ")
            if(attendence=='p' or attendence=='P'):
                student[i][1]=True
            elif(attendence=='a' or attendence=='A'):
                student[i][1]=False
            else:
                print("Invalid!")
                exit(1)
    elif(choice==3):
            for i in range(len(student)):
                if(student[i][1]==True):
                    print(f"{student[i][0]}=Present")
                else:
                    print(f"{student[i][0]}=Absent")
    elif(choice==4):
        for i in range(len(student)):
            if(student[i][1]==False):
                print(student[i][0])
    elif(choice==5):
        a=0
        p=0
        for i in range(len(student)):
            if(student[i][1]==True):
                p+=1

        percentage=(p/(len(student)))/100
        print(percentage)
    elif(choice==6):
        itretor=0


