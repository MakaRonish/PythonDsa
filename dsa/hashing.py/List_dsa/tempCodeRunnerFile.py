
def mores(nums):
    candidate=nums[0]
    count=0
    for i in range(len(nums)):
        if nums[i]==candidate:
            count+=1
        else:
            count-=1
        # if count==0:
        #     candidate=nums[i]
        #     count+=1
        if count==0:
            candidate=nums[i+1]
    return candidate

print(mores([5,2,5,1,5]))
