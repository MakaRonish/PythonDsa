class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        pointer = 0
        while True:
            if nums[zero] != 0 and zero < len(nums)-1:
                zero += 1
            if nums[pointer] == 0 and pointer < len(nums)-1:
                pointer += 1
            if zero > pointer:
                pointer += 1
            else:
                nums[zero], nums[pointer] = nums[pointer], nums[zero]
            if pointer >= len(nums) - 1:
                break
        return nums


a = Solution()
print(
    a.moveZeroes(
        [0,0,0,0,0,0]
    )
)



