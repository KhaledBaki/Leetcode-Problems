class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        counter =  0

        # Get all zero instances
        while ( i < len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                counter += 1
                i -= 1
            i += 1
        
        # Add all zero instances to the back
        while (counter > 0):
            nums.append(0)
            counter -= 1
