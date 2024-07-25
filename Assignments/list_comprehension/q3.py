lst = [i for i in range(1, 11)]


def last(n: int):
    result = []
    result = lst[-n::]
    print(result)


last(4)
