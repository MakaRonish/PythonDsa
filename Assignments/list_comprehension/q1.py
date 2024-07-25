lst = [i for i in range(1, 11)]


def slice(start: int, end: int):
     
    print(lst[start : end + 1 :])


print(lst)
slice(1, 5)
