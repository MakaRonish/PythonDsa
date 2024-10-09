# not best cause if the ith is already 0 it will change to 1
# this is for toggle
def clear(n, i):
    return n ^ (1 << i)


def clear2(n, i):
    return n & (~(1 << i))


print(clear(8, 3))
print(clear2(8, 3))
