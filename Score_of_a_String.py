class Solution(object):
    def scoreOfString(self, s):
        s = list(s)
        s = [ord(c) for c in s]

        total = 0
        for i in range(len(s) - 1):
            total += abs(s[i] - s[i + 1])
        
        return total
