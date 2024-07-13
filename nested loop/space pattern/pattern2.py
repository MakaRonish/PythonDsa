def pattern(n:int):
    for i in range(n,0,-1):
        for j in range(i,1,-1):
            print(" ",end=" ")
        for k in range(n,i-1,-1):
            print(k,end=" ")
        print()

pattern(5)