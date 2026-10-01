class Solution(object):
    def setZeroes(self, matrix):
        zeroLocation = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]  == 0:
                    zeroLocation.append([i,j])
        
        for pt in zeroLocation:
            for j in range(len(matrix[0])):
                matrix[pt[0]][j] = 0

            for i in range(len(matrix)):
                matrix[i][pt[1]] = 0
