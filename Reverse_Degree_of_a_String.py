class Solution(object):
    def reverseDegree(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s = list(s)
        total = 0

        for i in range(len(s)):
            total += (i + 1) * (26 - alphabet.index(s[i]))
        
        return total
