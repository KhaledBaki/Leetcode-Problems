class Solution(object):
    def checkIfPangram(self, sentence):
        sentence = set(sentence)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet = set(alphabet)

        return sentence == alphabet
