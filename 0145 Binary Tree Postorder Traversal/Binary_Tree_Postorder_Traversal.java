import java.util.List;
import java.util.LinkedList;
class Solution {
    public List<Integer> list = new LinkedList<>();
    public List<Integer> postorderTraversal(TreeNode root) {
        helper(root);
        return list;
    }
    public void helper(TreeNode root){
        if(root == null){
            return;
        }
        helper(root.left);
        helper(root.right);
        list.add(root.val);
    }
}
