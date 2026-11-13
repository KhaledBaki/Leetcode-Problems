class Solution(object):
    def searchBST(self, root, val):
        
        # Edge case 1 where root is null
        if root == None:
            return None
        
        # Base case where we find the value of the node
        if root.val == val:
            return root

        # Since we cant stack two returns over each other we checkout the left subtree without returning anything
        left = self.searchBST(root.left, val)

        # Return it if there is something
        if left != None:
            return left

        # Explore the right subpath
        return self.searchBST(root.right, val)
