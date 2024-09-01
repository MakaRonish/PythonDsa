class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=1
        n=len(nums)
        while zero<n-1 or one<n-1:
            while nums[zero]!=0:
                if nums[zero]==2:
                    a=nums.pop(zero)
                    nums.append(a)
                    
                else:
                    zero+=1
            while nums[one]!=1:
                if nums[one]==2:
                    a=nums.pop(one)
                    nums.append(a)
                    
                else:
                    one+=1
            if zero>one:
                nums[zero],nums[one]=nums[one],nums[zero]
            else:
                zero+=1

        return nums
    

a=Solution()
print(a.sortColors([2,0,2,1,1,0]))

