class Solution(object):
    def maxProduct(self, nums):

        # Sorts the numbers in decreasing order
        nums = sorted(nums, reverse = True)

        return (nums[0] - 1) * (nums[1] - 1)
