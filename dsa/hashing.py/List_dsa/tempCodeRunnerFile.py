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
    new=nums[len(nums)-1:ind:-1]
    for i in range(ind+1,len(nums)):
        nums[i]=new[i]
    return nums

print(nextPer([5,4,7,5,3,2]))