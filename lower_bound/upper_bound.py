l = [1, 5, 6, 6, 6, 6, 6, 7, 9, 9, 9, 10, 11, 14, 14]


def upper_bound(target, l):
    low = 0
    high = len(l) - 1
    up = "not available"
    while low <= high:
        middle = (low + high) // 2
        if l[middle] > target:
            high = middle - 1
            up = middle
        else:
            low = middle + 1

    return up


print(upper_bound(7, l))
