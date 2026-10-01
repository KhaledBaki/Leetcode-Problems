class Solution(object):
    def findNumbers(self, nums):
        output = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                output += 1
        return output
