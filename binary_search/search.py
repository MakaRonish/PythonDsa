l = [2, 4, 6, 7, 10, 11, 16, 18]


def find_index(num: int, l: list) -> tuple:
    low = 0
    high = len(l) - 1
    index = None
    loop_run = 0
    while high >= low:
        loop_run += 1
        middle = (low + high) // 2
        if l[middle] > num:
            high = middle - 1
        elif l[middle] < num:
            low = middle + 1
        else:
            index = middle
            return index, loop_run

    return num, " not in the list"


print(find_index(2, l))
