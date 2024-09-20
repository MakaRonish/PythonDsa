# Complete this function
class Solution:
    def floorSqrt(self, n):
        # Your code here
        ans = 0
        for i in range(1, (n // 2 + 1)):
            if i**2 <= n:
                ans = i
        return ans


a = Solution()
print(a.floorSqrt(99))

# better


def square(n):
    if n == 1:
        return 1

    low = 0
    high = n
    ans = 0
    while low <= high:
        middle = (low + high) // 2
        if middle**2 <= n:
            low = middle + 1
            ans = middle
        else:
            high = middle - 1
    return ans


print(square(100))
