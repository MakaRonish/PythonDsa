class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        minimum = nums[(low + high) // 2]
        while low <= high:
            middle = (low + high) // 2
            if nums[low] <= nums[middle]:
                if minimum < nums[middle]:
                    minimum = nums[middle]
                low = middle + 1
            else:
                high = middle - 1
            if nums[middle] < minimum:
                minimum = nums[middle]
        return minimum


a = Solution()
print(a.findMin([4, 5, 6, 7, 0, 1, 2]))
