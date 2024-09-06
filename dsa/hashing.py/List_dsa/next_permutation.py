class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n<=1:
            return
        break_point=nums[-1]
        index=-1
        for i in range(-1,-n-1,-1):
            if nums[i]<break_point:
                index=i
                break
            else:
                break_point=nums[i]
        if index!=-1:
            new=nums[index+1:]
            number=nums[index]
            numbers=[]
            for i in new:
                if i>number:
                    numbers.append(i)
            min_num_index=nums.index(min(numbers))
            nums[index],nums[min_num_index]=nums[min_num_index],nums[index]
            new=nums[index+1:]
            for i in range(-1,-len(new)-1,-1):
                index+=1
                nums[index]=new[i]
        else:
            new=nums[-1::-1]
            for i in range(len(new)):
                nums[i]=new[i]
        
        






a=Solution()
a.nextPermutation([2,1,5,4,3,0,0])


##solution
def nextPer(nums):
    n=len(nums)
    ind=-1
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            ind=i
            break
    if ind==-1:
        nums.reverse()
        return
    for i in range(n-1,ind,-1):
        if nums[i]>nums[ind]:
            nums[i],nums[ind]=nums[ind],nums[i]
            break
    nums[:]=nums[:ind+1]+nums[len(nums)-1:ind:-1]
    return nums

print(nextPer([5,4,7,5,3,2]))

                


