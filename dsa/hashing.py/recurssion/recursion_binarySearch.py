arr=[1, 3, 5, 7, 9, 11, 13]
def binary_search(arr:list,target,left=0,right=len(arr)-1):
    middle=(left+right)//2
    if arr[middle]>target:
        return binary_search(arr,target,left,middle-1)
    elif arr[middle]<target:
        return binary_search(arr,target,middle+1,right)
    elif arr[middle]==target:
        return middle
    elif left>=len(arr) or right<=0:
        return -1



print(binary_search([1, 3, 5, 7, 9, 11, 13],11))
    

