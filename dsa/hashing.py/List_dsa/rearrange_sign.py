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
    while True:
        if nums[p]<0:
            p+=1
        if nums[n]>0:
            n+=1
        if nums[p]>0 and nums[n]<0:
            final.append(nums[p])
            final.append(nums[n])
            p+=1
            n+=1

        


