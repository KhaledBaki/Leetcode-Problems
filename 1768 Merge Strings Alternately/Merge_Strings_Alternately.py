class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        result = ""

        # Converting to char array
        word1 = list(word1)
        word2 = list(word2)

        # Counters
        i = 0
        j = 0

        # Loops through the two arrays
        while (i < len(word1)) or (j < len(word2)):
            if (i < len(word1)) and (j < len(word2)):
                result = result + str(word1[i]) + str(word2[j])
                i += 1
                j += 1
            
            elif i < len(word1):
                result = result + str(word1[i])
                i += 1
            
            elif i < len(word2):
                result = result + str(word2[j])
                j += 1
                
        return result
            
