two_D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for i in range(len(two_D)):
    for j in range(len(two_D[i])):
        print(two_D[j][i], end=" ")
    print()

sum = 0
for i in two_D:
    for j in i:
        print(j, end=" ")
    print(" ")
for i in two_D:
    for j in i:
        sum += j
print(sum)
for i in two_D:
    sum2 = 0
    for j in i:
        sum2 += j
    print(sum2)


for i in range(len(two_D)):
    for j in range(len(two_D[i])):
        if i == j:
            print(two_D[i][j])

for i in range(len(two_D)):
    for j in range(len(two_D[i])):
        if i + j == len(two_D) - 1:
            print(two_D[i][j])


two_D = [
    [1, 2, 3, 4],
    [4, 5, 6, 4],
    [7, 8, 9, 4],
    [10, 11, 12, 4],
]
for i in range(len(two_D)):
    for k in range(i):
        print("*", end=" ")
    for j in range(i, len(two_D)):
        print(two_D[i][j], end=" ")
    print()

for i in range(len(two_D)):
    for j in range(len(two_D[i])):
        if j > i:
            print(two_D[i][j], end=" ")
        else:
            print("#", end=" ")
    print()
for i in range(len(two_D)):
    for j in range(len(two_D[i])):
        if j <= i:
            print(two_D[i][j], end=" ")
        else:
            print("#", end=" ")
    print()
