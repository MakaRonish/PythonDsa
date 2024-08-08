class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        dic={}
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in range(1,P+1):
            a=dic.get(i,0)
            print(a,end=" ")

s=Solution()
s.frequencyCount([2,3,2,3,5],5,5)