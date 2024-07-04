#more than 2 

age:int=int(input("Enter your age:"))
if age>18:
    print("adult")
elif age<17 and age>13:
    print("teenager")
else:
    print("child")


age:int=int(input("Enter your age:"))    
if age<60:
    print("fail")
elif age<70 and age>60:
    print("D")
elif age<80 and age>70:
    print("C")
elif age<90 and age>80:
    print("B")
else:
    print("A")