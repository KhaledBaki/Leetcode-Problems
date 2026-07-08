class Solution(object):
    def searchInsert(self, nums, target):
        
        try:
            # Basic python list method
            return nums.index(target)
        
        # .index() throws an exception of ValueError in target not in list
        except ValueError:

            # Edge case where index goes outside list (Upper)
            if nums[len(nums) - 1] < target:
                return len(nums)
            
            # Edge case where index goes outside list (Lower)
            elif nums[0] > target:
                return 0

            # Upper Half of list
            elif nums[len(nums) / 2] < target:
                for i in range(len(nums) / 2, len(nums)):
                    if (nums[i] < target) and (target < nums[i+1]):
                        return i + 1
            
            # Lower Half 
            elif nums[len(nums) / 2] > target:

                for i in range(0, len(nums) / 2):
                    if (nums[i] < target) and (target < nums[i+1]):
                        return i + 1
                    
        # Placeholder
        return 0
        
