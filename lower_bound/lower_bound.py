l = [1, 3, 5, 7, 9]
target = 6


def lower_bound_with_binary(l, target):
    low = 0
    high = len(l) - 1
    low_b = "not available"
    while low <= high:
        middle = (low + high) // 2
        if target <= l[middle]:
            high = middle - 1
            low_b = middle
        else:
            low = middle + 1
    return low_b


print(lower_bound_with_binary(l, 1))


def lower_bound(target):
    lb = len(l)
    for i in range(len(l)):
        if l[i] >= target:
            return i
    return lb


print(lower_bound(9))


def lower_bound_proper(target, l):
    low = 0
    high = len(l) - 1
    lb = len(l)
    while low <= high:
        middle = (low + high) // 2
        if l[middle] >= target:
            lb = middle
            high = middle - 1
        else:
            low = middle + 1
    return lb


def higher_bound_proper(target, l):
    low = 0
    high = len(l) - 1
    hb = len(l)
    while low <= high:
        middle = (low + high) // 2
        if l[middle] >= target:
            lb = middle
            high = middle - 1
        else:
            low = middle + 1
    return lb


print(lower_bound_proper(4, l))
