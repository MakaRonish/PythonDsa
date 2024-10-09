def remove(n: int):
    for i in range(65):
        if n & 1 << i > 0:
            index = i
            break
    return n ^ (1 << index)


def remove_and(n: int):
    for i in range(65):
        if n & 1 << i > 0:
            index = i
            break
    return n & ~(1 << index)


##Optimal
def remove_optima(n: int):
    return n & n - 1
