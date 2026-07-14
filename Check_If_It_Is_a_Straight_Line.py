class Solution(object):
    def checkStraightLine(self, coordinates):
        
        # Automatically Assume a line if only two points
        if len(coordinates) == 2:
            return True

        # Sometime the slope is undefined
        try:
            # Base Slope use float to avoid integer division
            slope = float((coordinates[1][1] - coordinates[0][1])) / float((coordinates[1][0] - coordinates[0][0]))

            # Loop through and get all the slopes
            for coord in range(len(coordinates) - 1):
                if float(coordinates[coord + 1][1] - coordinates[coord][1]) / float(coordinates[coord + 1][0] - coordinates[coord][0])  != slope:
                    return False

        except ZeroDivisionError: 

            # Make sure that there is a consistency in the x values
            for coord in range(len(coordinates) - 1):
                if coordinates[coord + 1][0] - coordinates[coord][0] != 0:
                    return False
        
        # Return true if nothing fails
        return True

        
