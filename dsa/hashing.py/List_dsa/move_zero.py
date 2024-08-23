class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros,number=0,0
        while True:
            if nums[zeros]!=0 and zeros < len(nums):
                zeros+=1
            if nums[number]==0 and number<len(nums):
                number+=1
            if zeros<number:
                nums[zeros],nums[number]=nums[number],nums[zeros]
            else:
                number+=1
            if zeros>=len(nums) and number>=len(nums):
                break
        return nums
    
a=Solution()
print(a.moveZeroes([1,0,1]))


            
            