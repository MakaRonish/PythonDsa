def factor(num:int)->None:
    i=1
    while i<=num:
        if (num/2)<i and i!=num:
            pass
        elif num%i==0:
            print(i,end=" ")
        i+=1
    
factor(100)
#effecient way
def factor1(num:int)->None:
    i=1
    while i<=num//2:
        if num%i==0:
            print(i,end=" ")

        i+=1
    print(num)
factor1(100)

#moreefficient
def factor2(num:int):
    i=1

    while True:
        if num%i==0:
            print(i,end=" ")
            x=int(num/i)
            if x==i:
                break
            else:
                print(x,end=" ")
        i+=1
        
factor2(100)