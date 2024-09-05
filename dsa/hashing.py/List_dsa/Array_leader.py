def array_leader(nums):
    for i in range(len(nums)):
        leader=True
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                leader=False
                break
        if leader:
            print(nums[i],end=" ")

array_leader([16,17,4,3,5,2])

#better:
def leader(arr,n):
    result=[arr[-1]]
    max=arr[-1]
    for i in range(-2,-n-1,-1):
        if arr[i]>=max:
            max=arr[i]
            result.append(max)
    new=result[-1::-1]
    return new

print(leader([16,17,4,3,5,2],6))

        
