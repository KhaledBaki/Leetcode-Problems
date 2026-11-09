class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        if nums[0] != 0:
            return 0
        return nums[len(nums) - 1] + 1
