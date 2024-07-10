# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()

def pattern(row:int)->None:
    for i in range(1,row+1):
        for j in range(1,6):
            print("1",end=" ")
        print()

row=int(input())
pattern(row)
