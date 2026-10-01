class Solution(object):
    def isPalindrome(self, s):
        stripped = []
        s = list(s)
        for char in s:
            if char.isalnum():
                stripped.append(char.lower())
        
        m = len(stripped) - 1
        
        for i in range(len(stripped) / 2):
            if stripped[i] != stripped[m - i]:
                return False
        return True
