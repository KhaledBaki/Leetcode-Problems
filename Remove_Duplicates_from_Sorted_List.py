class Solution(object):
    def deleteDuplicates(self, head):
        cursor = head
        while cursor and cursor.next:
            if cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return head
