class Solution(object):
    def addDigits(self, num):
        digits = [int(d) for d in str(num)]
        result  = 0

        for i in range(len(digits)):
            result = result + digits[i]
        
        # If you're reading this, I spent a good 15 MINS, questioning reality, and what kept crashing this was the float division, so I added .0 to each

        # Base case
        if result / 9.0 <= 1.0:
            return result

        # Recurssive call
        else:  
            return self.addDigits(result)
        
