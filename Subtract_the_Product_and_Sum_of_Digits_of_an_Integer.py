class Solution(object):
    def subtractProductAndSum(self, n):
        n = list(str(n))
        n = [int(i) for i in n]
        prod = 1
        addition = 0

        for num in n:
            prod *= num
            addition += num
        
        return prod - addition
