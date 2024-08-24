class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        removed=[]
        for i in range(k):
            a=nums.pop(-1)
            removed.append(a)
            nums.insert(0,removed[-1])

        
        

        return nums
    

a=Solution()
k=3
nums=[1,2,3,4,5,6,7]
new=nums[:-k]
print(new)


print(a.rotate(nums,3))


def rotate(nums,k):
    k=k%len(nums)
    back=nums[:-k]
    for i in back:
        nums.append(i)
        nums.pop(0)
    return nums

print(rotate([1,2,3,4,5,6,7],3))




        