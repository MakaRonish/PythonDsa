def findUnion(arr1,arr2,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    result=[]
    pointer_1=0
    pointer_2=0
    size=len(arr1)
    size2=len(arr2)
    while pointer_1<=n-1 or pointer_2<=m-1:
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
        if pointer_1>n-1:
            while pointer_2<=m-1:
                if result[-1]<arr2[pointer_2]:
                    result.append(arr2[pointer_2])
                    pointer_2+=1
                else:
                    pointer_2+=1
        if pointer_2>m-1:
            while pointer_1<=n-1:
                if result[-1]<arr1[pointer_1]:
                    result.append(arr1[pointer_1])
                    pointer_1+=1
                else:
                    pointer_1+=1

    return result

print(findUnion([-5,-4,-1,1,7],[-3,0,1,8],5,4))