# num1:int=int(input("enter a number"))
# num2:int=int(input("enter a number2"))
# if num1%num2==0:
#     print(f"{num1} is divided by {num2}")

# numofclass:int=int(input("NUmber of classes:"))
# Attendence:int=int(input("NUmber of Attendence:"))
# Attendence_percentage:float=float((Attendence/numofclass)*100)
# if Attendence_percentage>=75:
#     print("you are allow to sit in exam")
# else:
#     print("you are not allow to sit in exam")
# print(f"your attendence percentage is {Attendence_percentage}")

# num:int=int(input("ENter a number="))
# if (num%2==0 and num%3==0) and num%8!=0:
#     print(f"{num} is divisible by 2 and 3 but not 8")
# else:
#     print("nooo")


# bill:float=float(input("enter the bill amount: "))
# discount:int=0
# if bill>50000:
#     discount=30
# elif bill>40000 and bill<49999:
#     discount=25
# elif bill>30000 and bill<39999:
#     discount=20
# elif bill>10000 and bill<29999:
#     discount=10
# else:
#     discount=0
# total_bill:float=float(bill-(discount/100)*bill)
# print(f"you got {discount} discount")
# print(f"The total bill is {total_bill}")


# num1:int=int(input("enter a number:"))
# num2:int=int(input("enter a number:"))
# num3:int=int(input("enter a number:"))
# num4:int=int(input("enter a number:"))
# if num1<num2 and num1<num3 and num1<num4:
#     print(f"{num1} is the smallest")
# elif num2<num1 and num2<num3 and num2<num4:
#     print(f"{num2} is the smallest")
# elif num3<num2 and num3<num1 and num3<num4:
#     print(f"{num3} is the smallest")
# else:
#     print(f"{num4} is the smallest")

# salary:int=int(input("enter your salary:"))
# if salary>50000:
#     increase:int=20
# elif salary>20000:
#     increase:int=15
# elif salary>10000:
#     increase:int=10
# else:
#     increase:int=5

# new_salary:float=float(salary+(increase/100)*salary)
# print(f"The new salary after {increase}increment is {new_salary}")

year:int=int(input("enter a year"))
if (year%4==0 and year%100)and not(year%4==0 and year%400)==0:
    print(f"{year} year is not a leap year")
else:
    print(f"{year} year is a leap year")
    