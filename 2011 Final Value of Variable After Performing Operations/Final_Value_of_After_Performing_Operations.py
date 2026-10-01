class Solution(object):
    def finalValueAfterOperations(self, operations):
        total = 0
        for opp in operations:
            opp = opp.strip("X")

            if opp == "++":
                total += 1
            else:
                total -= 1
        
        return total
