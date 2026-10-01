class Solution(object):
    def findTheDifference(self, s, t):

        # Converts to list of chars
        s = list(s)

        # Converts char to ASCII value array
        s = [ord(term) for term in s]
        
        # ASCII Sum for S
        resultForS = 0

        # Converts to list of chars
        t = list(t)

        # Converts char to ASCII value array
        t = [ord(term) for term in t]

        # ASCII Sum for T
        resultForT = 0

        for term in t:
            resultForT += term
        
        for term in s:
            resultForS += term
        
        # Subtract, take positive, convert to char, convert to string
        return str(chr(abs(resultForS - resultForT)))
