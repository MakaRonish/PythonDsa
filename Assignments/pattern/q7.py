def pattern(n:int)->None:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print() 
pattern(5)