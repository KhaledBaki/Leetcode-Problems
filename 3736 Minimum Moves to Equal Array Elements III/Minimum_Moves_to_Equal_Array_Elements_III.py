class Solution(object):
    def minMoves(self, nums):
        largest = nums[0]

        # find the largest
        for num in nums:
            if num > largest:
                largest = num
        
        output = 0

        # do the basic math
        for num in nums:
            output += largest - num
        return output
