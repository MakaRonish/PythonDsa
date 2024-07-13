def pattern(n:int)->None:
    for i in range(1,n//2+2):
        for j in range(i,n//2+1):
            print("a",end=" ")
        print()

pattern(5)