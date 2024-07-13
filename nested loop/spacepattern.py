def pattern(n:int):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i+j>n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def pattern2(n:int):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(1,i+1):
            print("*",end=" ")
        print()

    else: 
        print("do you like the pattern?")
            

pattern(10)
pattern2(10)