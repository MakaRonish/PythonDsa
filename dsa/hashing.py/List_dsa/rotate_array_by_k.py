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
new=nums[-1:-k:-1]
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

#slicong
def rot(nums,k):
    nums[:]=nums[-k:]+nums[:-k]
    print(nums)

rot([1,2,3,4,5,6,7,8],5)


#optimal 
def reverse_arr(arr,i,j):
    while j>i:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
   


def rotated_by(arr,k):
    k=k%len(arr)
    reverse_arr(arr,i=len(arr)-k,j=len(arr)-1)
    reverse_arr(arr,i=0,j=len(arr)-1-k)
    reverse_arr(arr,i=0,j=len(arr)-1)
    print(arr)

rotated_by([1,2,3,4,5,6],6)





        