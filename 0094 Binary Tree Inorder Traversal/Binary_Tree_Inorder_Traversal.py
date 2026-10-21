class Solution(object):
    
    
    def inorderTraversal(self, root):
        output = []

        def helper(root):
            if root == None:
                return output

            if root.left != None:
                helper(root.left)
            
            output.append(root.val)

            if root.right != None:
                helper(root.right)

        helper(root)
        return output
