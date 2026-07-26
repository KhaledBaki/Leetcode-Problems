class Solution(object):
    def maximumWealth(self, accounts):
        largest = sum(accounts[0])
        for i in range(1, len(accounts)):
            if sum(accounts[i]) > largest:
                largest = sum(accounts[i])
        
        return largest
