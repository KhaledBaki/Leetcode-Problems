class Solution(object):
    def sumAndMultiply(self, n):
        if n == 0:
            return 0

        # Converting to list of chars
        n = str(n)
        n = list(n)

        # Sum and Concatenated number
        total = 0
        concatenated = ""

        for num in n:
            if num != '0':
                total += int(num)
                concatenated += str(num)

        return int(concatenated) * total
