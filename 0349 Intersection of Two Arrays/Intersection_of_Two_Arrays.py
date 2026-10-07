class Solution(object):
    def intersection(self, nums1, nums2):
        
        # Convert to set and return thier union
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersection = nums1.intersection(nums2)
        
        output = []

        for num in intersection:
            output.append(num)
        return output
