class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        leftSol = moves.replace("_", "L")
        ansL = 0

        rightSol = moves.replace("_", "R")
        ansR = 0

        for move in list(leftSol):
            if move == 'L':
                ansL -= 1
            else:
                ansL += 1
        
        for move in list(rightSol):
            if move == 'R':
                ansR += 1
            else:
                ansR -= 1
        
        ansL = abs(ansL)
        ansR = abs(ansR)
        if ansL > ansR:
            return ansL
        
        return ansR
