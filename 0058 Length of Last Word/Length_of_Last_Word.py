class Solution(object):
    def lengthOfLastWord(self, s):

        # Clears spaces from both sides
        s = s.strip()

        # Splits at the occurence of a space
        s = s.split(" ")

        # Return the last element length
        return len(s[len(s) - 1])
