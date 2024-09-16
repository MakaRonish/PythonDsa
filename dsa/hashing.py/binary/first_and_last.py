class Solution(object):

    # wrong
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        start = -1
        end = -1
        while low <= high:
            middle = (low + high) // 2
            if nums[low] == nums[high] == target:
                return [low, high]
            elif nums[middle] <= target and nums[low] != target:
                low = middle + 1
            elif nums[middle] >= target and nums[high] != target:
                high = middle - 1
        return [start, end]


def searchRange(nums, target):
    low = 0
    high = len(nums) - 1
    start = -1
    end = -1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] < target:
            low = middle + 1
        elif nums[middle] > target:
            high = middle - 1
        else:
            high = middle - 1
            start = middle
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] < target:
            low = middle + 1
        elif nums[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
            ceil = middle
    return [start, end]


print(ord("a"))


def searchRange_combine(nums, target):
    low = 0
    high = len(nums) - 1
    floor = -1
    ceil = -1
    start = -1
    end = -1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] <= target:
            low = middle + 1
            ceil = middle
        if nums[middle] >= target:
            high = middle - 1
            floor = middle

    if nums[floor] == target:
        start = floor
    if nums[ceil] == target:
        end = ceil
    return [start, end]


print(searchRange_combine([5, 7, 7, 8, 8, 10], 8))
