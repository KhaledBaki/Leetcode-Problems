class Solution(object):
    def isPalindrome(self, head):
        
        arr = []
        curr = head

        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        
        n = len(arr)
        for i in range(len(arr)):
            if arr[i] != arr[n - i - 1]:
                return False
        
        return True
