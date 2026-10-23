class Solution(object):
    def isPerfectSquare(self, num):
        maximum = num // 2
        minimum = 1
        mid = (maximum + minimum) // 2

        if num == 1:
            return True
        
        while minimum <= maximum:
            mid = (maximum + minimum) // 2
            if mid * mid == num:
                return True
            
            if mid * mid > num:
                maximum = mid - 1
                
            else:
                minimum = mid + 1

        return False
