# check if the ith bit is set or not


def checker(n: int, i: int) -> bool:
    and_value = 1 << i
    ans = n & and_value
    if ans > 0:
        return True
    return False


def right__shift_checker(n: int, i: int) -> bool:
    if (n >> i) & 1 == 0:
        return False
    return True


print(checker(13, 1))
print(right__shift_checker(13, 1))
