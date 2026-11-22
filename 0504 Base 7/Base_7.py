class Solution(object):
    def convertToBase7(self, num):
        
        # Edge case 0
        if num == 0:
            return "0"
        
        output = ""
        isNegative = False

        if num < 0:
            isNegative = True
        
        num = abs(num)
        
        while num > 0:
            output += str(num % 7)
            num //= 7
        
        if isNegative:
            output += "-"
            return "".join(reversed(output))
        
        return "".join(reversed(output))
