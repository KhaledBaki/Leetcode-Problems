class Solution(object):
    def sortList(self, head):
        nodes = []

        curr = head
        while curr != None:
            nodes.append(curr.val)
            curr = curr.next
        
        nodes = sorted(nodes)
        curr = head

        i = 0
        while curr != None:
            curr.val = nodes[i]
            i += 1
            curr = curr.next
            
        return head
