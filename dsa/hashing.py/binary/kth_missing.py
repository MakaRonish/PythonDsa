class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        missing = []
        set_arr = set(arr)
        while i <= max(set_arr):
            if i not in set_arr:
                missing.append(i)
            i += 1
        if k > len(missing) - 1:
            return missing[-1] + k
        else:
            return missing[k]
