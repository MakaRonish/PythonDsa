def storingsum(arr):
    dic={}
    a=0
    sum=0
    for i in arr:
        sum+=i
        dic[a]=sum
        a+=1
    return dic




# def longest_sum(arr,k):
#     dic=storingsum(arr)
#     length=0
#     sum=0
#     for i in range(len(arr)):
#         sum+=arr[i]
#         if sum==k:
#             length=i+1
#         rem=sum-k
#         if rem in dic.values():

            
        
        
        


# print(longest_sum([1 ,4, 3, 3, 5, 5],16))



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
            L=i-sum_map[rem]
            max_length=max(max_length,L)
        if sum not in sum_map:
            sum_map[sum]=i
    return max_length

#only positive

# def positive(arr,k):
#     j=0
#     length=0
#     sum=0
#     for i in range(len(arr)):
#         sum+=arr[i]
#         while sum<=k:
#             j+=1
#             sum+=arr[j]


def positive(arr,k):
    sum=arr[0]
    i=0
    r=0
    max=0

    while  r<len(arr)-1:
        
        while sum<=k and r<len(arr)-1:
            r+=1
            sum+=arr[r]
            if sum==k and max<(r-i+1):
                max=r-i+1
        
        while sum>k and i<len(arr):
            sum=sum-arr[i]
            i+=1
            if sum==k and max<(r-i+1):
                max=r-i+1
    return max

print(positive([1, 2, 3, 4],10))
        

            


        










