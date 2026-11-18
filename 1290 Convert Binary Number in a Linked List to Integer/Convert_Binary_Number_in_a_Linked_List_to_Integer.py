class Solution(object):
    def getDecimalValue(self, head):
        
        size = 0
        total = 0
        curr = head 
        while curr != None:
            curr = curr.next
            size += 1
        
        curr = head
        while curr != None:
            if curr.val == 1:
                total += pow(2, size - 1)
            size -=1
            curr = curr.next
        
        return total
