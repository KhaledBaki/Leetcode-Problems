class Solution(object):
    def findMissingElements(self, nums):
        nums = sorted(nums)
        A = nums[0]
        B = nums[len(nums) - 1]
        missingList = []
        for i in range(B - A):
            if A + i not in nums:
                missingList.append(A + i)

        return missingList
