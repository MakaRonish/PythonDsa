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