def maxin(numss):
    low = 0
    high = len(numss) - 1
    maxi = float("-inf")
    while low <= high:
        middle = (low + high) // 2
        if numss[low] <= numss[middle]:
            maxi = max(maxi, numss[middle])
            low = middle + 1
        else:
            maxi = max(maxi, numss[high])
            high = middle - 1
    return maxi


print(maxin([4, 5, 5, 6, 1, 2, 3]))
