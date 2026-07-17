class Solution(object):
    def average(self, salary):
        total = 0
        for s in salary:

            # Check if they're max or min
            if s != max(salary) and s != min(salary):

                # Sum them up
                total += s
        
        # Subtract 2 to account for the max and min terms
        return float(total) / (len(salary) - 2)
