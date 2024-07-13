# def pattern(n:int):
#     for i in range(1,n+1):
#         for j in range(i,n):
#             print(" ",end=" ")
#         for k in range(1,i*2):
#             print("*",end=" ")
#         print()
# pattern(10)

# def pattern2(n:int):
#     for i in range(1,n+1):
#         for j in range(i,n):
#             print(" ",end=" ")
#         for k in range(1,i+1):
#             print("*",end=" ")
#         for l in range(1,i):
#             print("*",end=" ")
#         print()

# pattern2(9)
# def pattern3(n:int):
#     for i in range(n,0,-1):
#         for k in range(1,n-i+2):
#             print("1",end=" ")
#         for j in range(1,i*2):
#             print("*",end=" ")
#         print()
# pattern3(4)


def star(n: int):
    n2 = n // 2
    n = n - n2
    for i in range(1, n + 1):
        for j in range(i, n):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print("*", end=" ")
        print()
    for i in range(n2, 0, -1):
        for k in range(1, n2 - i + 2):
            print(" ", end=" ")
        for j in range(1, i * 2):
            print("*", end=" ")
        print()


star(13)

for i in range(9//2,0,-1):
    for j in range(1,5-i+1):
        print(" ",end=" ")
    for k in range(1,i*2):
        print("*",end=" ")
    print()