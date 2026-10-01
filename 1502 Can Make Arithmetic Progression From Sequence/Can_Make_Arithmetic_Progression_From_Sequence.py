class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)

        # Initial difference
        diff = abs(arr[0] - arr[1])

        for i in range(len(arr) - 1):

            # Remaining difference
            if abs(arr[i] - arr[i+1]) != diff:
                return False
        
        # Base case
        return True
