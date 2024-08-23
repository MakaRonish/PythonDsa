def smallest_index(arr):
    return arr.index(min(arr))

def rorated(arr):
    index=smallest_index(arr)
    sorted=True
    while True:
        if index+1==len(arr):
            index=-1
        if arr[index]>arr[index+1]:
            sorted=False
            break
        if index+1==smallest_index(arr)-1:
            break
        index+=1
    return sorted
index=smallest_index([6,7,8,4])
s=rorated([6,7,8,4])
if s==True:
    print(f"rotation={index}")


#optimal

arr=[5,10,20,66,2,3]
def rora(arr):
    rotation=0
    for i in range(0,len(arr)-1):
        if arr[i]>arr[(i+1)]:
            rotation+=1
        if rotation>1:
            return False
    return True

print(rora(arr))


        

def sorted(arr):
    i=0
    sorted=True
    while i<len(arr)-2:
        if arr[i]>arr[i+1]:
            sorted=False
            break
        i+=1
    return sorted

print(sorted([2,3,4,4,4,4]))

