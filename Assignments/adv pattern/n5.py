def pattern(n:int)->None:
    n2=n//2
    n1=n-n2
    for i in range(1,n1+1):
        for j in range(i,n1):
            print(" ",end=" ")
        for k in range(1,i+1):
            print(k,end=" ")
        print()
    for i in range(n2,0,-1):
        for j in range(i,n2+1):
            print(" ",end=" ")
        for k in range(1,i+1):
            print(k,end=" ")
        print()

pattern(9)