def quick_sort(arr,low,high):
    pivot = arr[0]
    low=0
    high=len(arr)-1
    while True:
        if arr[low]<=pivot:
            low+=1
        if arr[high]>pivot:
            high-=1
        if high<low:
            arr[0],arr[high]=arr[high],pivot
            break
        if arr[low]>pivot and arr[high]<pivot:
            arr[low],arr[high]=arr[high],arr[low]
        
        
        
    return high



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

    return arr


def quick_s(arr,low,high):
    if low<high:
        ind=quick_sort(arr,low,high)
        quick_s(arr,low,ind-1)
        quick_s(arr,ind+1,high)
    return arr



print(quick_sort([9,8,7,6,5,4,3,2,1]))
print(partation([9,8,7,6,5,4,3,2,1],0,8))
        

            


            



