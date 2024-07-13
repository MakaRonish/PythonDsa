def diamond(n:int)->None:
    n2=n//2
    n1=n-n2
    for i in range(1,n1+1):
        for j in range(i,n1):
            print(" ",end=" ")
        for k in range(1,i*2):
            print("x",end=" ")
        print()
    for i in range(1,n2+1):
        for j in range(1,i+1):
            print(" ",end=" ")
        for k in range(1,-2*i+n+1):
            print("x",end=" ")
        print()

diamond(7)

n = int(input("Enter number of lines = "))
for i in range(1, (n // 2 + 1) + 1):
    for j in range(1, (n // 2 + 1) - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
for i in range(n // 2, 0, -1):
    for j in range(1, (n // 2 + 1) - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()