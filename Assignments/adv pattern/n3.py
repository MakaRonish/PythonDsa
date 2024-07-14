def pattern(n:int):
    n2=n//2
    n1=n-n2
    for i in range(n1,0,-1):
        for j in range(i,n1+1):
            print(j,end=" ")
        print()
    for i in range(1,n2+1):
        for j in range(i+1,n1+1):
            print(j,end=" ")
        print()
pattern(9)