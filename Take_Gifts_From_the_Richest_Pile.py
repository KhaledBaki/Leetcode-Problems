import numpy as np
class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            gifts = sorted(gifts, reverse = True)
            gifts[0] = math.floor(math.sqrt(gifts[0]))
        
        gifts = np.array(gifts)
        
        return int(np.sum(gifts))
