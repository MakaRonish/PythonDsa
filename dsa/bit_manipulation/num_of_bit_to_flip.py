class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ans = start ^ goal
        c = 0
        # basic counting 1 in ans
        for i in range(32):  # 32 bits 0 included
            if ans & (1 << i) != 0:
                c += 1

        # optimal
        c = 1
        while ans != 1:
            rem = ans % 2
            if rem == 1:
                c += 1
            ans = ans // 2
