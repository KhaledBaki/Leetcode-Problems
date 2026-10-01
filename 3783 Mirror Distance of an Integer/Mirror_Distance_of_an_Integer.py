class Solution(object):
    def mirrorDistance(self, n):
        
        # Base number
        original = n

        # Slicing number to digits
        n = str(n)
        n = list(n)

        # Reversing list in place
        n.reverse()

        # Concatenating reversed list
        reversedNumber = ""
        for i in range(len(n)):
            reversedNumber += n[i]
        
        # Returning required formula
        return abs(original - int(reversedNumber))
