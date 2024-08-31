class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

def dic_method(nums,target):
    dic={}
    for i in range(len(nums)):
        if nums[i] not in dic.keys():
            dic[nums[i]]=i
        needed=target-nums[i]
        if needed in dic:
            return [dic[needed],i]
        

print(dic_method([2,7,11,15],9))
                