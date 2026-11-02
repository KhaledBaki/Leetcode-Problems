class Solution(object):
    def isStrictlyPalindromic(self, n):
        array = []
        original = n
        if n == 0:
            return True
        
        while n > 0:
            array.append(n % (original - 2))
            n //= (original - 2)
        
        m = len(array) - 1
        for i in range(len(array) / 2):
            if array[i] != array[m - i]:
                return False
        
        return True
