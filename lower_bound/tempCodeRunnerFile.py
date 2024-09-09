l = [1, 3, 5, 7, 9]
target = 6


def lower_bound_with_binary(l, target):
    low = 0
    high = len(l) - 1
    low_b=len(l)
    while low < high:
        middle = (low + high)//2
        if target<=l[middle]:
            high=middle-1
            low_b=middle
        else:
            low=middle+1
    return low_b

print(lower_bound_with_binary(l,100))