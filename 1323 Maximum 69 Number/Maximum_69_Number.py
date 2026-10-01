class Solution(object):
    def maximum69Number (self, nums):
        nums = str(nums)
        nums = list(nums)
        output = ""
        firstSix = False

        for i in range(len(nums)):
            if not firstSix and nums[i] == '6':
                nums[i] = '9'
                firstSix = True

            output += nums[i]
        
        return int(output)
