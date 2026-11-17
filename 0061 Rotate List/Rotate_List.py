class Solution(object):
    def rotateRight(self, head, k):
        if head == None or k == 0 or head.next == None:
            return head
        
        # Used to find the size of the list
        size = 0
        curr = head

        # Gets size
        while curr != None:
            size += 1
            curr = curr.next

        # Cleeaers unecessary rotations
        k = k % size

        if k == 0:
            return head
        # Places a fixed tail index location
        tailIndex = size - k


        tailP = head
        for i in range(tailIndex - 1):
            tailP = tailP.next
        
        newHead = tailP.next
        tailP.next = None

        cursor = newHead

        while cursor.next != None:
            cursor = cursor.next

        cursor.next = head

        return newHead
