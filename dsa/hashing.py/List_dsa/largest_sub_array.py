class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=0
                for k in range(i,j+1):
                    sum+=nums[k]
                if sum>max_sum:
                    max_sum=sum
        return max_sum
    


a=Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

#brute better
def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=0
        for i in range(len(nums)):
            total=0
            for j in range(i,len(nums)):
                 total+=nums[j]
                 if total>max_sum:
                      max_sum=total
                 
        return max_sum


#kandane' algorithm
""" 
keep on updating the sum and make it 0 when not benificial
"""

def maxSubArray_kandaneAlgorithm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            sum+=nums[i]
            if sum<0:
                sum=0
            if max_sum<sum:
                 max_sum=sum
        return max_sum
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
                first_index=i+1
            if max_sum<sum:
                 max_sum=sum
                 second_index=i
        return max_sum,nums[first_index:second_index+1]

print(maxSubArray_kandaneAlgorithm_withIndex([5,7,8,9,-10,5,4,3,2,-100,5,7,8,100]))
            


            

        