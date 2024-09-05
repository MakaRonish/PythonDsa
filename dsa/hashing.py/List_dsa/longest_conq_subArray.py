class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[]
        for i in range(len(nums)):
            a=nums[i]
            while True:
                if a+1 in nums:
                    
