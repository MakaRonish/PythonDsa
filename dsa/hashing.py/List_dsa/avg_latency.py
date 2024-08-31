def avg(arr,k):
    sum=0
    for i in range(-1,-k-1):
        sum+=arr[i]
    return sum/k


