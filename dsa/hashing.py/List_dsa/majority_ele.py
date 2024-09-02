def majority(nums):
    dic={}
    maj=0
    ele=None
    for i in nums:
        dic[i]=dic.get(i,0)+1
    for i in dic:
        if dic[i]>maj:
            maj=dic[i]
            ele=i
    return maj

print(majority([3,2,3]))



dic={"a":1}
for i in dic:
    print(dic[i])

#Mores voting algorithm

def mores(nums):
    candidate=nums[0]
    count=0
    for i in range(len(nums)):
        if nums[i]==candidate:
            count+=1
        else:
            count-=1
        if count==0:
            candidate=nums[i]
            count+=1

    return candidate

print(mores([5,2,5,1,5]))

    