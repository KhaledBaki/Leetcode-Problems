class Solution(object):
    def isUgly(self, n):
        if n == 1:
            return True
        
        if n == 0:
            return False
            
        d5 = True
        d3 = True
        d2 = True

        
        while d2 != False or d3 != False or d5 != False:
            if n % 5 == 0:
                n /= 5
            else:
                d5 = False

            if n % 3 == 0:
                n /= 3
            else:
                d3 = False

            if n % 2 == 0:
                n /= 2  
            else:
                d2 = False

        return n == 1
