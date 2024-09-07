class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        set_nums = set(nums)

        for i in range(len(nums)):
            num = nums[i]
            sub = [num]
            j = 0
            while True:
                if num + 1 in set_nums:
                    num = num + 1
                    sub.append(num)
                else:
                    break
            if len(sub) > len(result):
                result = sub[:]
        return len(result)


def longest(nums):
    longest = float("-inf")
    set_nums = set(nums)
    for i in range(len(nums)):
        num = nums[i]
        c = 1
        while True:
            if num + 1 in set_nums:
                num = num + 1
                c += 1
            else:
                break
        if c > longest:
            longest = c
    return longest if longest != float("-inf") else 0


print(longest([]))


# by sorting
# a = []
# print(a[0])


# better solution
def longest1(nums):
    if len(nums) < 2:
        return len(nums)
    nums.sort()
    length = 1
    ele = nums[0]
    count = 1
    i = 1
    while i < len(nums):
        if nums[i] == ele + 1:
            count += 1
            if count > length:
                length = count
        elif nums[i] == ele:
            pass
        else:
            count = 1

        ele = nums[i]
        i += 1
    return length


# def longest_hash(nums):
#     dic = {}
#     for i in range(len(nums)):
#         dic[nums[i]] = dic.get(nums[i], 0) + 1
#     length = 0
#     count = 1
#     for key in dic.keys():
#         if key + 1 in dic:
#             count += 1
#             if count > length:
#                 length = count
#         else:
#             count = 1
#     return length


# print(longest_hash([100, 4, 200, 1, 3, 2]))


# # optimal solution

# dic = {1: "a", 2: "b", 3: "c"}

# for i in dic.keys():
#     print(i)
#     if (i + 1) in dic:
#         print("yes")


# optimal


def set_method(nums):
    if len(nums) < 2:
        return len(nums)
    set_nums = set(nums)

    total = 1
    for i in set_nums:

        if i - 1 not in nums:
            count = 1
            while True:
                if i + 1 in nums:
                    count += 1
                else:
                    break
            if count > total:
                total = count
    return total


set_1 = {1, 2, 3}
for i in set_1:
    print(i)
