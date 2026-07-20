import numpy as np
class Solution(object):
    def repeatedSubstringPattern(self, s):
        
        # Building blocks for the splitter
        chars = list(s)

        # Initial Splitter
        term = ""

        for i in range(len(s) // 2):

            # Add to splitter
            term += str(chars[i])

            # Split
            a = s.split(term)

            # Convert to numpy array
            numpyArr = np.array(a)

            # Check equality
            if np.all(numpyArr == ""):
                return True
        
        # Base case
        return False




        
