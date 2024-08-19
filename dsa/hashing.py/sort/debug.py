def sort(arr1,arr2):
    i=0
    j=0
    sorted_arr=[]
    while True:
        if i>=len(arr1) and j>=len(arr2):
            break
        elif i>=len(arr1):
            sorted_arr.append(arr2[j])
            j+=1
        elif j>=len(arr2):
            sorted_arr.append(arr1[i])
            i+=1 
        elif arr1[i]<arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            sorted_arr.append(arr2[j])
            j+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
            
            
    return sorted_arr

def merge_sort(list):
    if len(list)==1:
        return list
    half=len(list)//2
    left_side=list[:half]
    right_side=list[half:]
    left=merge_sort(left_side)
    right=merge_sort(right_side)
    return sort(left,right)
    
a=merge_sort([10,9,8,7,6,5,4,-99])
print(a)
