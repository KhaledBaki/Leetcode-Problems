class Solution {
    private TreeNode rightTree = null;
    private TreeNode curr;
    public TreeNode increasingBST(TreeNode original) {
        helper(original);
        return rightTree;
    }
    private void helper(TreeNode root) {
        if (root == null) {
            return;
        }
        
        helper(root.left);
        
        if (rightTree == null) {
            rightTree = new TreeNode(root.val);
            curr = rightTree;
        } 
        else {
            curr.right = new TreeNode(root.val);
            curr = curr.right; 
        }
        
        helper(root.right);
    }
}
