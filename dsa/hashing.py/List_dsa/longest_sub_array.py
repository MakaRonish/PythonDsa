# def longest_sub(arr,k):
#     i=0
#     length=0
#     while i<len(arr)-1:
#         if arr[i]<k:
#             j=i+1
#             sum=arr[i]
#             c=1
#             while sum<k and j<len(arr):
#                 c+=1
#                 sum+=arr[j]
#                 j+=1
#         i+=1
#         if length<c and sum==k:
#             length=c
#     return length if length!=0 else 0
def longest_sub(arr,k):
    i=0
    length=0
    while i<len(arr):
        sum=arr[i]
        c=1
        if sum==k:
            if length<c:
                length=c
        else: 
            for j in range(i+1,len(arr)):
                sum+=arr[j]
                if sum==k and length<(j-i+1):
                    length=j-i+1
                        
                        
        i+=1
    return length
    
            


    
print(longest_sub([8,-9,10,-2,-10,6,18,17],17))


def sub_array(arr,n,k):
    i=0
    length=0
    for j in range(n):
        sum=arr[j]

        pointer=j+1
        if j==n-1:
            if sum==k and length<1:
                length=1
        else:
            for l in range(j,pointer+1):
                sum+=arr[l]
                if sum==k and length<l-j+1:
                    length=l-j+1
    return length
                
