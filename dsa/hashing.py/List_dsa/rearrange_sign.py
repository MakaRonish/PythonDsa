class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive=[]
        negative=[]
        final=[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
        for p,n in zip(positive,negative):
            final.append(p)
            final.append(n)



def reargange(nums):
    p=0
    n=0
    final=[]
    while p<len(nums) and n<len(nums):
        while nums[p]<0 and p<len(nums)-1:
            p+=1
        while nums[n]>0 and n<len(nums)-1:
            n+=1
        if p<len(nums) and n<len(nums):
            final.append(nums[p])
            final.append(nums[n])
            p+=1
            n+=1
    return final

reargange([-1,1,2,3,-2,-3])


def pointer(nums):
    p=0
    n=1
    result=[0]*len(nums)
    for i in range(len(nums)):
        if nums[i]>0:
            result[p]=nums[i]
            p+=2
        else:
            result[n]=nums[i]
            n+=2


        


