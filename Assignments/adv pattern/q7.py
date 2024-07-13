def pattern(n:int):
    x=n
    for i in range(n,0,-1):
        for j in range(1,i):
            print(" ",end=" ")
        for k in range(1,(-2*i+12)):
            print(i,end=" ")
        print()
pattern(6)