def pattern(num:int):
    for i in range(1,num+1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

pattern(5)