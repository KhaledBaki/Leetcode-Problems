class Solution(object):
    def digitFrequencyScore(self, n):
        n = str(n)
        n = list(n)
        n = [int(i) for i in n]
        return sum(n)
