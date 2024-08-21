class Solution:
    def largest(self,arr):
        large=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>large:
                large=arr[i]
        return large
    def print2largest(self, arr):
        large=self.largest(arr)
        print(large)
        second_large=float("-inf")
        for i in arr:
            if i>second_large and i<large:
                second_large=i
        return -1 if second_large==float("-inf") else second_large
        
a=Solution()
l=[1,2,3,4,5,6,7,8,9]
print(a.print2largest(l))

#better solution



large=float("-inf")
second_large=float("-inf")
for i in l:
    if i>large:
        second_large=large
        large=i
    elif i>second_large and i!=large:
        second_large=i
print(second_large)