def pivot_place(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while True:
        while i<high and arr[i]<=pivot:
            i+=1
        while j>low  and arr[j]>=pivot:
            j-=1
        if i>=j:
            break
        arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],pivot
    return j


def quick_sort(arr,low,high):
    if high<0 or low>high:
        return
    index=pivot_place(arr,low,high)
    quick_sort(arr,low,index-1)
    quick_sort(arr,index+1,high)
    return arr
print(quick_sort([4,6,2,5,7,9,1,3],0,7))