def dic_method(nums,target):
    dic={}
    for i in range(len(nums)):
        if dic[nums[i]] not in dic:
            dic[nums[i]]=i
        needed=target-nums[i]
        if needed in dic:
            return [dic[needed],i]
        

print(dic_method([2,7,11,15],9))