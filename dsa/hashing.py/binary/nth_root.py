class Solution:
    def NthRoot(self, n, m):
        # Code here
        low = 0
        high = m
        root = n
        while low <= high:
            middle = (low + high) // 2
            if middle**n == m:
                return middle
            elif middle**n < m:
                low = middle + 1
            else:
                high = middle - 1
        return -1


print(())
