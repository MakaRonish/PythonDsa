class Solution(object):
    def right_weight(self, weights, capacity):
        i = 0
        day_taken = 0
        total = 0

        while i < len(weights):
            total += weights[i]
            if total == capacity:
                day_taken += 1
                total = 0
            elif total > capacity:
                day_taken += 1
                total = weights[i]
            i += 1

        return day_taken if total == 0 else day_taken + 1

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)
        capacity = 0
        while low <= high:
            middle = (low + high) // 2
            if self.right_weight(weights, middle) <= days:
                capacity = middle
                high = middle - 1
            else:
                low = middle + 1
        return capacity


a = Solution()
print(a.shipWithinDays([1, 2, 3, 1, 1], 4))
