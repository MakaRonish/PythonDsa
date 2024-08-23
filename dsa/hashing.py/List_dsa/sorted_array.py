class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted=nums[:]
        sorted.sort()
        for i in range(len(nums)):
            same=True
            k=i
            for j in range(len(nums)):
                if k==len(nums):
                    k=0
                
                if sorted[k]==nums[j]:
                    k+=1
                    continue
                else:
                    same=False
                    break
            if same:
                return same
        return same


def check(arr):
    small=arr[0]
    index=0
    sorted=False
    for i in range(1,len(arr)):
        if arr[i]<small:
            small=arr[i]
            index=i

    Order=arr[index+1]
    for i in range(len(arr)):
        if index==len(arr):
            index=0
        if arr[index]<=Order:
            sorted=True
            if index+1==len(arr):
                Order=arr[index]
                index+=1
            else:
                index+=1
                Order=arr[index+1]
        else:
            return False
    return sorted



    


# class Solution2(object):
#     def check(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         sorted=nums[:]
#         sorted.sort()
#         for i in range(len(nums)):
#             same=True
#             k=i
#             for j in range(len(nums)):
#                 if k==len(nums):
#                     k=0
                
#                 if sorted[k]==nums[j]:
#                     k+=1
#                     continue
#                 else:
#                     same=False
#                     break
#             if same:
#                 return same
#         return same
        
#         for i in range(1,len(nums)):
#             if nums[i]<smallest:
#                 smallest=nums[i]
#                 index=i

                
#         j=0
#         for i in range(len(nums)):
#             if j==len(nums):
#                 j=0
#             if sorted[i]==nums[(j+index)%len(nums)]:
#                 j+=1
#                 continue
#             else:
#                 return False
#         return True
    
# l=[1,2,3]
# l2=l.copy()

# l2.pop()
# print(l)
# print(l2)
a=Solution()
l=[1,2,3,4,5]
l1=[5,1,2,3,4]
print(a.check(l1))