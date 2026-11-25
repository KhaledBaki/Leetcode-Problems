class Solution(object):
    def transformArray(self, nums):
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even += 1
            
        for i in range(len(nums)):
            if even != 0:
                even -= 1
                nums[i] = 0
                continue
            nums[i] = 1
        return nums
