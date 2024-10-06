class Solution:
    def checker(self, k, stalls, distance):
        i = 0
        counter = 1
        j = 0
        while j < len(stalls) - 1:
            j += 1
            if stalls[j] - stalls[i] >= distance:
                counter += 1
                i = j
            if counter == k:
                return True

    def solve(self, n, k, stalls):
        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0]
        while low <= high:
            middle = (low + high) // 2
            result = self.checker(k, stalls, middle)
            if result:
                low = middle + 1
            else:
                high = middle - 1
        return high


a = Solution()
print(a.solve(6, 4, [0, 3, 4, 7, 9, 10]))
