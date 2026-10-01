# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rem = 0
        cursorOne = l1
        cursorTwo = l2

        # Initiating the output singly linked-list
        digit = (cursorOne.val + cursorTwo.val + rem) % 10
        rem = (cursorOne.val + cursorTwo.val + rem) // 10
        cursorOne = cursorOne.next
        cursorTwo = cursorTwo.next
        actualTotal = ListNode(digit)
        
        # Cursor of the output singly linked-list
        total = actualTotal
        
        while cursorOne != None and cursorTwo != None:
            digit = (cursorOne.val + cursorTwo.val + rem) % 10
            rem = (cursorOne.val + cursorTwo.val + rem) // 10
            total.next = ListNode(digit)
            
            total = total.next
            cursorOne = cursorOne.next
            cursorTwo = cursorTwo.next
        
        while cursorOne != None :
            digit = (cursorOne.val + rem) % 10
            rem = (cursorOne.val + rem) // 10

            total.next = ListNode(digit)
            total = total.next
            cursorOne = cursorOne.next
        
        while cursorTwo != None :
            digit = (cursorTwo.val + rem) % 10
            rem = (cursorTwo.val + rem) // 10

            total.next = ListNode(digit)
            total = total.next
            cursorTwo = cursorTwo.next

        if rem != 0:
            total.next = ListNode(rem)
            
        return actualTotal

        
        
        
