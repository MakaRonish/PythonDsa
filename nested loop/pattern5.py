def pattern(num:int)->None:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def pattern2(num:int)->None:
    for i in range(num,0,-1):
        for j in range(1,7-i):
            print(j,end=" ")
        print()

pattern(10)
pattern2(5)

