import math


class Solution(object):
    def sum_(self, nums, middle):
        total = 0
        for i in range(len(nums)):
            total += math.ceil(nums[i] / middle)
        return total

    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high = max(nums)
        small_div = 0
        while low <= high:
            middle = (low + high) // 2
            if self.sum_(nums, middle) <= threshold:
                high = middle - 1
                small_div = middle
            else:
                low = middle + 1
        return small_div


a = Solution()
print(a.smallestDivisor([44, 22, 33, 11, 1], 5))
