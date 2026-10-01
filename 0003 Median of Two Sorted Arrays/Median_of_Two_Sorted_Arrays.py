import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        return np.median(combined)
