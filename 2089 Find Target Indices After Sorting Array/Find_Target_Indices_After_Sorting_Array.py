class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)

        output = []
        foundFirst = False
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
                foundFirst = True
                
            elif nums[i] != target and foundFirst:
                break
        
        return output
