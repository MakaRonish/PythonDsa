def power_of_2(n: int):
    return n & (n - 1) == 0


print(power_of_2())
