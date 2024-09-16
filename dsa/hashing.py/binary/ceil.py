class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        low = 0
        high = len(arr) - 1
        arr.sort()
        floor = -1
        ceil = -1
        while low <= high:
            middle = (low + high) // 2
            if arr[middle] <= x:
                floor = arr[middle]
                low = middle + 1
            else:
                high = middle - 1
        low = 0
        high = len(arr) - 1

        while low <= high:
            middle = (low + high) // 2
            if arr[middle] >= x:
                ceil = arr[middle]
                high = middle - 1
            else:
                low = middle + 1
        return [ceil, floor]


def floor(x, arr):
    low = 0
    high = len(arr) - 1
    arr.sort()
    floor = -1
    ceil = -1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] <= x:
            floor = arr[middle]
            low = middle + 1
        if arr[middle] >= x:
            ceil = arr[middle]
            high = middle - 1

    return [ceil, floor]
