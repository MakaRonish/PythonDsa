def Union(arr1,arr2):
    result=[]
    pointer_1=0
    pointer_2=0
    size=len(arr1)
    while pointer_1<size or pointer_2<size:
        if arr1[pointer_1]<arr2[pointer_2]:
            if len(result)==0:
                result.append(arr1[pointer_1])
                pointer_1+=1
            elif result[-1]>=arr1[pointer_1]:
                pointer_1+=1
            else:
                result.append(arr1[pointer_1])
                pointer_1+=1
        elif arr1[pointer_1]>arr2[pointer_2]:
            if len(result)==0:
                result.append(arr2[pointer_2])
                pointer_2+=1
            elif result[-1]>=arr2[pointer_2]:
                pointer_2+=1
            else:
                result.append(arr2[pointer_2])
                pointer_2+=1
        else:
            if len(result)==0:
                result.append(arr2[pointer_2])
                pointer_2+=1
            elif result[-1]>=arr2[pointer_2]:
                pointer_2+=1
            else:
                result.append(arr2[pointer_2])
                pointer_2+=1
        if pointer_1>=size-1:
            while pointer_2<=size-1:
                if result[-1]<arr2[pointer_2]:
                    result.append(arr2[pointer_2])
                    pointer_2+=1
                else:
                    pointer_2+=1
        if pointer_2>=size-1:
            while pointer_1<=size-1:
                if result[-1]<arr1[pointer_1]:
                    result.append(arr1[pointer_1])
                    pointer_1+=1
                else:
                    pointer_1+=1

        return result
    
print(Union([1,2,3,4,5],[1,2,3,4,5]))