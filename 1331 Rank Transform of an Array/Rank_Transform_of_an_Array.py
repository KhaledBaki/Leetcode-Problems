# This is the O(n^2) solution, it passed all the test cases but it couldnt complete the last test case in time
class Solution(object):
    def arrayRankTransform(self, arr):
        
        original = arr
        arr = sorted(list(set(arr)))
        output = []

        for num in original:
            output.append(arr.index(num) + 1)
        return output
