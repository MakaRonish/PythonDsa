def single(nums: list):
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans
