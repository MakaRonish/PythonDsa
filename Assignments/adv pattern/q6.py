def pattern(n:int):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(1,i*2):
            print("x",end=" ")
        print()
pattern(6)