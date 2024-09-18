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
