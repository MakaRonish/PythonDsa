class Solution(object):
    def num_of_days(self, weights, capacity):
        Total_day = 0
        ship = 0
        weights_sum = 0
        while ship < len(weights):
            weights_sum += weights[ship]
            if weights_sum > capacity:
                weights_sum = weights[ship]
                Total_day += 1
            ship += 1
        if weights_sum > 0:
            Total_day += 1
        return Total_day

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = min(weights)
        high = len(weights) * max(weights)
        ans = 0
        while low <= high:
            middle = (low + high) // 2
            total_day = self.num_of_days(weights, middle)
            if total_day <= days:
                ans = middle
                high = middle - 1
            else:
                low = middle + 1
        return ans


a = Solution()
print(a.num_of_days([1, 2, 3, 1, 1], 3))
