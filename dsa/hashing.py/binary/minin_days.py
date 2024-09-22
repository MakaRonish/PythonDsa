class Solution(object):
    def bouk_maker(self, bloomDay, m, k, n):
        no_of_book = 0
        f = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= n:
                f += 1
                if f == k:
                    f = 0
                    no_of_book += 1
            else:
                f = 0
        if no_of_book >= m:
            return True

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if k * m > len(bloomDay):
            return -1
        mini = min(bloomDay)
        maxi = max(bloomDay)
        no_of_days = 0
        while mini <= maxi:
            middle = (mini + maxi) // 2
            if self.bouk_maker(bloomDay, m, k, middle):
                maxi = middle - 1
                no_of_days = middle
            else:
                mini = middle + 1
        return no_of_days


a = Solution()
print(a.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
