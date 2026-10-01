class Solution(object):
    def separateDigits(self, nums):
        array = []
        nums = [list(str(num)) for num in nums]
        for num in nums:
            for n in num:
                array.append(int(n))
        return array
