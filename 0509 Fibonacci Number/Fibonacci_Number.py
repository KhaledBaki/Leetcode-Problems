class Solution(object):
    def fib(self, n):
        term1 = 0
        term2 = 1

        if n == 0:
            return 0

        if n == 1:
            return 1


        temp = term1 + term2
        for i in range(n - 1):
            temp = term1 + term2
            term1 = term2
            term2 = temp
        return temp
