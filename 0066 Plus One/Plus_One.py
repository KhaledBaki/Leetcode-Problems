class Solution(object):
    def plusOne(self, digits):

        # Empty string
        s = ""

        # Go through digits
        for d in digits:

            # Concatenate string feature
            s += str(d)
        
        # Add one to the number
        s = int(s) + 1

        # Convert the number into a number array 
        return [int(d) for d in str(s)]
