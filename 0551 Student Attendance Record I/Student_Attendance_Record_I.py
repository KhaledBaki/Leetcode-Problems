class Solution(object):
    def checkRecord(self, s):
        s = list(s)
        aCount = 0
        for char in s:
            if char == 'A':
                aCount += 1
                if aCount >= 2:
                    return False
        
        for i in range(len(s) - 2):
            if s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
                return False

        return True
