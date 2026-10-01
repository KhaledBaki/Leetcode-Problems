class Solution:
    def findWords(self, words):
        output = []
        rowOne = "qwertyuiop"
        rowTwo = "asdfghjkl"
        rowThree = "zxcvbnm"

        
        # Covert to char array
        rowOne = set(rowOne)
        rowTwo = set(rowTwo)
        rowThree = set(rowThree)

        

        for i in range(len(words)):
            modifiedWord = set(words[i].lower())

            if modifiedWord <= rowOne:
                output.append(words[i])
            
            elif modifiedWord <= rowTwo:
                output.append(words[i])

            elif modifiedWord <= rowThree:
                output.append(words[i])
        
        return output
