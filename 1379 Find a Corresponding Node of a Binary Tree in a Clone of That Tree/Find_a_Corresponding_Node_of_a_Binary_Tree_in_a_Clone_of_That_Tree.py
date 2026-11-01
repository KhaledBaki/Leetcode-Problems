class Solution(object):

    # the strategy is to do a traversal
    def getTargetCopy(self, original, cloned, target):
        if original == None:
            return
        
        # check if we are at the same point as the target
        if original == target:
            return cloned
        
        # we store the left subtree so that the other return gets called aswell
        leftTree = self.getTargetCopy(original.left, cloned.left, target)

        # check if its NONE
        if leftTree != None:
            return leftTree

        # explore the right subtree
        return self.getTargetCopy(original.right, cloned.right, target)
