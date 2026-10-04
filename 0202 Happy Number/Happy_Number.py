class Solution(object):
    def isHappy(self, n):
        n = list(str(n))
        n = [int(i) for i in n]

        newNumber = 10
        while newNumber > 9:
            newNumber = 0
            for num in n:
                newNumber += num * num
            n = list(str(newNumber))
            n = [int(i) for i in n]
        
        if newNumber == 1 or newNumber == 7:
            return True
        
        return False
