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
            for j in range(i,len(arr)):
                sum=0
                for k in range(i,j+1):
                    sum+=arr[k]
                if sum==k and length<(i-j+1):
                    length=i-j+1
                        
                        
        i+=1
    return length
    
            


    
print(longest_sub([8,-9,10,-2,-10,6,18,17],17))
