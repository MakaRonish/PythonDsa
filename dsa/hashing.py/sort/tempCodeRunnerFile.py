def partation(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<pivot and i<high:
            i+=1
        while arr[j]>pivot and j<low:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]

    return j


def quick_s(arr,low,high):
    if low<high:
        ind=partation(arr,low,high)
        quick_s(arr,low,ind-1)
        quick_s(arr,ind+1,high)
    return arr


print(quick_s([4,3,9,8,1,2],0,5))