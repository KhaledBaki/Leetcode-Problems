class Solution(object):
    def checkDivisibility(self, n):
        original = n

        mult = 1
        n = list(str(n))
        n = [int(num) for num in n]

        for num in n:
            mult *= num

        return original % (sum(n) + mult) == 0
