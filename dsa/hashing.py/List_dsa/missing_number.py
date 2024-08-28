class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        for i in range(n):
            if i not in nums:
                return i
        return -1
def missingNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n=len(nums)
    sum_=sum(i for i in range(0,n+1))
    print(sum_)
    total=sum(i for i in nums)
    print(total)
    return sum_-total

print(missingNumber([0,1,2,3,5]))
    