def pattern(num:int)->None:
    for i in range(num,0,-1):
        for j in range(i,num+1):
            print(j,end=" ")
        print()
pattern(3)