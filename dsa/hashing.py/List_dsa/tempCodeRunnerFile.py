def positive(arr,k):
    sum=0
    i=0
    r=1
    max=0

    while i<len(arr) or r<len(arr):
        sum+=arr[i]
        while sum<=k and r<len(arr):
            sum+=arr[r]
            r+=1
            if sum==k and max<(r-i+1):
                max=r-i+1
        
        while sum>k and i<len(arr):
            sum=sum-arr[i]
            i+=1
            if sum==k and max<(r-i+1):
                max=r-i+1
    return max

print(positive([1,2,3,1,1,1,1,3,3],6))