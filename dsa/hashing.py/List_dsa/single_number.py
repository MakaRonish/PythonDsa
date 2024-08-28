def single(nums):
    dic={}
    for i in nums:
        dic[i]=dic.get(i,0)+1
    for key in dic.keys():
        if dic[key]==1:
            return key