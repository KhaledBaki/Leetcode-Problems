class Solution(object):
    def findWordsContaining(self, words, x):
        output = []
        for i in range(len(words)):
            if x in words[i]:
                output.append(i)
        return output
