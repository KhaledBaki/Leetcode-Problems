class Solution(object):
    def maxProduct(self, n):
        n = str(n)
        n = list(n)
        n = [int(d) for d in n]
        n = sorted(n, reverse = True)
        return n[0] * n[1]
