def pattern(n: int) -> None:
    n2 = n // 2
    n1 = n - n2
    print(n1, n2)
    for i in range(1, n1 + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    for i in range(n2, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()


pattern(9)
