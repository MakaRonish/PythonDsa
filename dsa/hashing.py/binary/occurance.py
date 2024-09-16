class Solution:
    def start(self, arr, x):
        low = 0
        high = len(arr) - 1
        strt = None
        while low <= high:
            middle = (low + high) // 2
            if arr[middle] == x:
                strt = middle
                high = middle - 1
            elif arr[middle] > x:
                high = middle - 1
            elif arr[middle] < x:
                low = middle + 1
        return strt

    def end(self, arr, x):
        low = 0
        high = len(arr) - 1
        end = None
        while low <= high:
            middle = (low + high) // 2
            if arr[middle] == x:
                end = middle
                low = middle + 1
            elif arr[middle] > x:
                high = middle - 1
            elif arr[middle] < x:
                low = middle + 1
        return end

    def count(self, arr, n, x):
        # code here
        start = self.start(arr, x)
        print(start)
        end = self.end(arr, x)
        print(end)
        if start != None:
            return end - start + 1
        else:
            return 0


a = Solution()
print(a.count([1, 1, 2, 2, 2, 2, 3], 7, 2))
