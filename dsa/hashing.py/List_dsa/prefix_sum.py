def storingsum(arr):
    dic={}
    a=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        dic[sum]=i
        a+=1
    return dic




def longest_sum(arr,k):
    dic=storingsum(arr)
    length=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==k:
            length=i+1   
        needed=sum-k
        a=dic.get(needed,True)
        if a:
            pass
        else:
            b=i-dic[needed]
            if length<b:
                length=b
    return length


print(longest_sum([1 ,4, 3, 3, 5, 5],16))



def long(arr,k):
    sum_map={}
    sum=0
    max_length=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==k:
            max_length=i+1
        rem=sum-k
        if rem in sum_map:
            L=i=sum_map[rem]
            max_length=max(max_length,L)
        if sum not in sum_map:
            sum_map[sum]=i
    return max_length






