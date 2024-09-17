class Solution:
    def findKRotation(self, arr):
        # code here
        low = 0
        high = len(arr) - 1
        mini = float("inf")
        while low <= high:
            middle = (low + high) // 2
            if arr[low] <= arr[middle]:
                mini = min(mini, arr[low])
                low = middle + 1
            else:
                mini = min(mini, arr[middle])
                high = middle - 1
        return arr.index(mini)
