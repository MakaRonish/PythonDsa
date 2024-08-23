def second_smallest(arr):
    smallest=float("inf")
    second_smallest=float("inf")
    for i in range(len(arr)):
        if arr[i]<smallest:
            second_smallest=smallest
            smallest=arr[i]
        elif arr[i]<second_smallest and arr[i]!=smallest:
            second_smallest=arr[i]
    return second_smallest

print(second_smallest([1,6,8,3,4,2,4,4,2,1]))