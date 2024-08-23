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