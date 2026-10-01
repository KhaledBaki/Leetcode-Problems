# My second "Two-Pointer" solution to this problem
class Solution(object):
    def hasCycle(self, head):
        cursor = head
        twoStepCursor = head
        
        while twoStepCursor and twoStepCursor.next:
            cursor = cursor.next
            twoStepCursor = twoStepCursor.next.next
            
            if cursor == twoStepCursor:
                return True

        return False
