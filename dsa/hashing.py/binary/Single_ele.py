class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while True:
            if i == len(nums) - 1:
                if nums[i] != nums[i - 1]:
                    return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]

            else:
                i += 2


# optimal soln


def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if middle % 2 == 0:

            if middle != 0 and nums[middle] == nums[middle - 1]:
                high = middle - 1
            elif middle != len(nums) - 1 and nums[middle] == nums[middle + 1]:
                low = middle + 1
            else:
                return nums[middle]
        else:
            if middle != 0 and nums[middle] == nums[middle - 1]:
                low = middle + 1
            elif middle != len(nums) - 1 and nums[middle] == nums[middle + 1]:
                high = middle - 1
            else:
                return nums[middle]


# print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))

# better


def singleNonDuplicate2(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] != nums[middle - 1] and (
            middle != len(nums) - 1 and nums[middle] != nums[middle + 1]
        ):
            return nums[middle]
        if nums[middle] == nums[middle - 1]:
            if middle % 2 == 0:
                low = middle + 1
            else:
                high = middle - 1
        else:
            if middle % 2 == 0:
                low = middle + 1
            else:
                high = middle - 1


print(singleNonDuplicate2([1, 1, 2, 2, 3, 3, 4, 4, 8]))
