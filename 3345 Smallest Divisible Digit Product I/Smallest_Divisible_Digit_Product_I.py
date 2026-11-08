class Solution(object):
    def smallestNumber(self, n, t):
        
        for i in range(10):
            initial = n
            multiplication = 1

            n += i
            n = list(str(n))
            n = [int(k) for k in n]

            for j in range(len(n)):
                multiplication *= n[j]

            if multiplication % t == 0:
                return initial + int(i)
            n = initial
