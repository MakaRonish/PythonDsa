import math


class Solution(object):
    def total_hours(self, piles: list, rate):
        total = 0
        for i in range(len(piles)):
            ans = math.ceil(piles[i] / rate)
            total += ans
        return total

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int

        """
        low = 1
        high = max(piles)
        while low <= high:
            middle = (low + high) // 2
            r = self.total_hours(piles, middle)
            if r == h:
                return middle
            elif r < h:
                high = middle - 1
            else:
                low = middle + 1


a = Solution()
print(a.minEatingSpeed([312884470], 312884470))
