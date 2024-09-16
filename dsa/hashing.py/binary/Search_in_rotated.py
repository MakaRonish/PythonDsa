class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[low] <= nums[middle]:
                if nums[low] <= target <= nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[middle] <= target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1

        return -1

    def search_dublicate(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            if nums[middle] == nums[low] == nums[high]:
                low += 1
                high -= 1

            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[low] <= nums[middle]:
                if nums[low] <= target <= nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            else:
                if nums[middle] <= target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1

        return -1


a = Solution()
print(a.search([1], 1))
