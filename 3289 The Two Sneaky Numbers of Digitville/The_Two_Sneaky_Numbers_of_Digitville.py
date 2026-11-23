class Solution(object):
    def getSneakyNumbers(self, nums):
        nums = sorted(nums)

        output = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                output.append(nums[i])
        return output
