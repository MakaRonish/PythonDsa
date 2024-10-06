def checker(arr, n, m, pages):
    students = 1
    pages_studens = 0
    for i in range(n):
        if pages_studens + arr[i] <= pages:
            pages_studens += arr[i]
        else:
            students += 1
            pages_studens = arr[i]

    return students


def findPages(arr, n: int, m: int) -> int:
    if m > n:
        return -1
    low = max(arr)
    high = sum(arr)
    while low <= high:
        middle = (low + high) // 2
        std_count = checker(arr, n, m, middle)
        if std_count <= m:
            high = middle - 1
        else:
            low = middle + 1
    return low


print(findPages([2, 8, 8, 4, 5], 5, 6))
