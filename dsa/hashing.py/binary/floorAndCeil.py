def getFloorAndCeil(a, n, x):
    # Write your code here.
    low = 0
    high = n - 1
    floor = -1
    ceil = -1
    while low <= high:
        middle = (low + high) // 2
        if a[middle] == x:
            return [a[middle], a[middle]]
        elif a[middle] < x:
            low = middle + 1
            floor = a[middle]
        elif a[middle] > x:
            high = middle - 1
            ceil = a[middle]
    return [floor, ceil]


a = {
    0: "6",
    1: "6",
    2: "7",
    3: "12",
    4: "16",
    5: "18",
    6: "19",
    7: "22",
    8: "23",
    9: "30",
}
