def pattern(n:int)->None:
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(i,0,-1):
            print(k,end=" ")
        print()
pattern(5)
