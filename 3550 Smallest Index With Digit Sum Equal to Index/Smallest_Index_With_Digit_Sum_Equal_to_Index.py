class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            
            if nums[i] < 10 and nums[i] == i:
                return i

            sumDigits = 0
            while nums[i] > 0:
                sumDigits += nums[i] % 10
                nums[i] /= 10
            if sumDigits == i:
                return i
        return -1
