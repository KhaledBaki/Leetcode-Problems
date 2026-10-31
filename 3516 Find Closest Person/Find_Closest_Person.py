class Solution(object):
    def findClosest(self, x, y, z):
        xSteps = abs(z - x)
        ySteps = abs(z - y)

        if xSteps == ySteps:
            return 0

        if xSteps < ySteps:
            return 1
        
        return 2
