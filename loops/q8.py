def evenCounter(num:int,num2:int)->None:
    count=0
    while num<=num2:
        if num%2==0:
            count+=1
        num+=1
    print(f"The total number of even numbers are {count}")

evenCounter(1,10)