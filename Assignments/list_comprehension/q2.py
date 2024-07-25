lst = [i for i in range(1, 21) if i % 2 == 0]


def slc(num: int) -> list:
    result = []
    result = lst[: -num - 1 : -1]
    return result


print(lst)
print(slc(4))
