class Solution(object):
    def runningSum(self, nums):
        total = 0
        output = []

        for num in nums:
            total += num
            output.append(total)
        return output
