def storingsum(arr):
    dic={}
    a=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        dic[sum]=i
        a+=1
    return dic

print(storingsum([10,5,2,7,1,9]))