def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    str_num = str(x)
    reversenum = int(str_num[::-1])
    if reversenum > 2147483647 or reversenum < -2147483648:
        return 0
    return reversenum


print(reverse(56789))


print(5 // 2)


class Solution:
    def lcmAndGcd(self, A, B):
        # code here
        factor_a = [A]
        factor_b = [B]
        factor = []

        for i in range(2, A // 2 + 1):
            if A % i == 0:
                factor_a.append(i)
        print(factor_a)
        for i in range(2, B // 2 + 1):
            if B % i == 0:
                factor_b.append(i)
        print(factor_b)
        factor = [value for value in factor_a if value in factor_b]
        print(factor)
        LCM = min(factor)
        GCM = max(factor)
        return [LCM, GCM]


a = Solution()
print(a.lcmAndGcd(5, 10))
