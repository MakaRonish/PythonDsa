def maxFre(l: list):
    rep = {}
    for i in l:
        rep[i] = rep.get(i, 0) + 1

    new = list(rep.items())
    max = float("-inf")

    for i in rep:
        if rep[i] > max:
            max = i

    return max


print(maxFre([4, 5, 6, 5, 4, 4, 7, 5, 5, 5, 5]))
