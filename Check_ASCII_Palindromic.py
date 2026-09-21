class Solution(object):
    def isPalindromic(self, s):
        s = list(s)
        binary = ""

        # Convert to ASCII
        s = [ord(i) for i in s]
        
        for num in s:
            for i in range(8):
                if num % 2 != 0:
                    binary += "1"
                else:
                    binary += "0"
                num //= 2
        
        for i in range(len(binary) // 2):
            if binary[i] != binary[len(binary) - i - 1]:
                return False

        return True
