def removeDuplicates( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[]
        for i in range(len(nums)):
            if nums[i] not in result:
                result.append(i)
            else:
                    
                nums=result
                print(nums)
                return len(nums)
            

def dubli(nums):
    j=0
    for i in range(1,len(nums)):
        a=nums[i]
        b=nums[j]
        if nums[i]!=nums[j]:
            nums[j+1]=nums[i]
            j+=1
    print(nums)
    return j+1

arr=[1,1,1,2,3,4,5]
dic={}
for i in range(0,len(arr)):
     dic[arr[i]]=0


i=0
for key in dic.keys():
     arr[i]=key
     i+=1

print(arr)
     


               
          

            
          
          



print(dubli([0,0,1,1,1,2,2,3,3,4]))