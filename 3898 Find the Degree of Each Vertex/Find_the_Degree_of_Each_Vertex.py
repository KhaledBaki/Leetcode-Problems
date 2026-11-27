class Solution(object):
    def findDegrees(self, matrix):
        output = []
        for i in range(len(matrix)):
            counter = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    counter += 1
            
            output.append(counter)
        
        return output
