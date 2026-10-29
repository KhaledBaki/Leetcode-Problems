class Solution(object):
    def getAllElements(self, root1, root2):
        list1 = []
        list2 = []
        def helper(root, listX):
            if root == None:
                return
            helper(root.left, listX)
            listX.append(root.val)
            helper(root.right, listX)
        helper(root1, list1)
        helper(root2, list2)
        
        list3 = list1 + list2
        return sorted(list3)
