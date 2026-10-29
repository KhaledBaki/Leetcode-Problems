class Solution {
    public int minDepth(TreeNode root) { 
        // Base case
        if (root == null){
            return 0;
        }
        
        // Skewed Case 1
        if (root.right == null){
            return minDepth(root.left) + 1;
        }

        // Skewed Case 2
        if (root.left == null){
            return minDepth(root.right) + 1;
        }

        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
