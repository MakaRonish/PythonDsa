def numbers(num1:int,num2:int)->None:
    if num1<num2:
        while num1<=num2:
            print(num1,end=" ")
            num1+=1
    else:
        while num2<=num1:
            print(num2,end=" ")
            num2+=1

numbers(10,20)
numbers(30,10)
