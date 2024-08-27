class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for i in range(N):
            if arr[i]==K:
                return i 
        return -1

a=Solution()
print(a.searchInSorted([1,2,3,4,7,8,9],7,9))