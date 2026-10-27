# Keeps track of the path we have
arrayList = []
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        # If we are at a dummy node we return false
        if root == None:
            return False
        
        # we add the current root
        global arrayList
        arrayList.append(root.val)
        
        # check if the node is a leaf node
        if root.left == None and root.right == None:

            # Check to see if the sum of the path adds up to the target
            isSame = (sum(arrayList) == targetSum)

            # Remove the leaf since we would have already explored that path
            arrayList.pop()

            return isSame
        
        # Recursively call to checkout left and right subtree paths
        foundMatch = self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        # This deletes the current node value since we are no longer using that branch
        arrayList.pop()

        return foundMatch
