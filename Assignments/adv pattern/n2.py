def pattern(num:int)->None:
    for i in range(1,num//2+2):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    for i in range(num//2,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

pattern(9)