class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        int remaining = targetSum;
        if (root == null){
            return false;
        }

        if(root.left == null && root.right == null){
            if (remaining == root.val){
                return true;
            }
        }
        remaining -= root.val;
        return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
    }
}
