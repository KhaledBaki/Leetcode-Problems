import re
class Solution(object):
    def strStr(self, haystack, needle):
        output = 0

        # Splitting the haystack at every occurence of needle (If exists)
        words = re.split(r"(" + needle + ")", haystack)

        # Go through the words
        for word in words:

            # Return once we hit output
            if word == needle:
                return output
            
            # Add the length of the word if not needle
            elif word != needle:
                output += len(word)
        
        # Base Case
        return -1
        
