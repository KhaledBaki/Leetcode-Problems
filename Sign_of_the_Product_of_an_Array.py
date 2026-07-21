class Solution(object):
    def arraySign(self, nums):
        base = 1
        for num in nums:
            if num == 0:
                return 0

            elif num < 0:
                base *= -1
                
        return base
