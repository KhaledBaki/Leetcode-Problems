class Solution(object):
    def getRow(self, rowIndex):
        output = []
        for i in range(rowIndex + 1):
            term = (math.factorial(rowIndex)) // (math.factorial(i) * math.factorial(rowIndex - i))
            output.append(term)
        return output
