def maxSubArray_kandaneAlgorithm_withIndex( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max_sum=float("-inf")
        first_index=0
        second_index=0
        for i in range(1,len(nums)):
            sum+=nums[i]
            if sum<0:
                sum=0
                first_index=i
            if max_sum<sum:
                 max_sum=sum
                 second_index=i
        return max_sum,[first_index,second_index]

print(maxSubArray_kandaneAlgorithm_withIndex([5,7,8,9,-10,5,4,3,2,-100,5,7,8,100]))