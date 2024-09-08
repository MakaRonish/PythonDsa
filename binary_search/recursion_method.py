l = [2, 4, 6, 7, 10, 11, 16, 18]


def index_find(num, l, low=0, high=None):
    if high is None:
        high = len(l) - 1

    if low > high:
        return None
    middle = (low + high) // 2
    if l[middle] > num:
        return index_find(num, l, low, middle - 1)

    elif l[middle] < num:
        return index_find(num, l, middle + 1, high)

    else:
        return middle


print(index_find(2, l))
