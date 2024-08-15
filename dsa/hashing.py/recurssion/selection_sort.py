#time complexity = o(n^2)
def selection_sort(arr:list,)->list:
    for i in range(len(arr)):
        min_value=arr[i]
        min_index=i
        for j in range(i,len(arr)):
            if arr[j]<min_value:
                min_value=arr[j]
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
    return arr

print(selection_sort([9,8,7,6,5,4,3,2,1]))
        
