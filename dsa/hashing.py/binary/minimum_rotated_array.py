class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mini = float("inf")
        while low <= high:
            middle = (low + high) // 2
            if nums[low] <= nums[middle]:
                mini = min(mini, nums[low])
                low = middle + 1
            else:
                mini = min(mini, nums[middle])
                high = middle - 1
        return mini


a = Solution()
print(a.findMin([4, 5, 6, 7, 0, 1, 2]))
