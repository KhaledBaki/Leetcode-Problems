class Solution(object):
    def mergeNodes(self, head):
        firstZero = False

        curr = head
        
        while curr.next.next != None:
            if not firstZero and curr.val == 0:
                firstZero = True
                curr.val = curr.next.val
                curr.next = curr.next.next

            elif firstZero and curr.next.val == 0:
                firstZero = False
                curr.next = curr.next.next
                
                
                curr = curr.next

            else:
                if curr.next.val == 0:
                    curr = curr.next

                else:   
                    curr.val += curr.next.val
                    curr.next = curr.next.next
                
        curr.next = None
        return head
