class Solution(object):
    def deleteNode(self, node):
        def swap(node1, node2):
            temp = node1
            node1.val = node2.val
            node2.val = temp.val
        
        curr = node

        while curr.next != None:
            swap(curr, curr.next)
            if curr.next.next == None:
                curr.next = None
                break

            curr = curr.next
