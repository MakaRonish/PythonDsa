# BRute
def peak(nums):
    if len(nums) == 1:
        return 0
    for i in range(len(nums)):
        if i == 0:
            if nums[i] > nums[i + 1]:
                return nums[i]
        elif i == len(nums) - 1:
            if nums[i] > nums[i - 1]:
                return nums[i]
        elif nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            return nums[i]


# optimal


def peark_binary(nums):
    if len(nums) == 1:
        return 0
    low = 0
    high = len(nums) - 1
    if nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] > nums[middle - 1] and nums[middle] > nums[middle + 1]:
            return middle
        if nums[middle] < nums[middle + 1]:
            low = middle + 1
        else:
            high = middle - 1
