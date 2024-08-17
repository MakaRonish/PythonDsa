l=[9,8,7,6,5,4,3,2,1]
def merge(l:list,):
    if len(l)<=1:
        return l
    div=(len(l))//2
    left=l[:(div)]
    right=l[div:]
    left_half=merge(left)
    right_half=merge(right)
    return sortSorting_arr(left_half,right_half)




def sortSorting_arr(l1,l2):
    result=[]
    i=0
    j=0
    while True:
        if i>=len(l1) and j>=len(l2):
            break
        if i>=len(l1):
            result.append(l2[j])
            j+=1
        elif j>=len(l2):
            result.append(l1[i])
            i+=1
        elif l1[i]<l2[j]:
            result.append(l1[i])
            i+=1
        elif l2[j]<l1[i]:
            result.append(l2[j])
            j+=1  
        elif l2[j]==l1[i]:
            result.append(l2[j])
            j+=1  
        
    return result

print(merge(l))




        


