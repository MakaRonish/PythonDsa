def rotate(nums,k):
    k=k%len(nums)
    back=nums[:-k]
    for i in back:
        nums.append(i)
        nums.pop(0)
    return nums

print(rotate([1,2,3,4,5,6,7],3))