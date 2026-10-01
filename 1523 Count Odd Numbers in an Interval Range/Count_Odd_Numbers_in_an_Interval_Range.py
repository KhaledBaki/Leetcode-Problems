class Solution(object):
    def countOdds(self, low, high):
        # Odd, Odd case
        if(low % 2 != 0) and (high % 2 != 0):
            return int(math.ceil(((high - low) / 2.0))) + 1

        # Rest of the cases
        return int(math.ceil((high - low) / 2.0))
