class Solution(object):
    def isMonotonic(self, nums):
        
        if len(nums) == 1:
            return True
        
        i = 0
        slope = nums[0] - nums[1]

        while slope == 0 and i < len(nums) - 1:
            slope = nums[i] - nums[i + 1]
            i += 1

        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i + 1] == 0:
                continue

            elif slope < 0 and (nums[i] - nums[i + 1]) > 0:
                return False

            elif slope > 0 and (nums[i] - nums[i + 1]) < 0:
                return False
