import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> list = new ArrayList<>();

    public int rangeSumBST(TreeNode root, int low, int high) {
        helper(root);
        int sum = 0;
        for(int i = 0; i < list.size(); i++){
            if(list.get(i) >= low && list.get(i) <= high){
                sum += list.get(i);
            }
        }
        return sum;
    }

    public void helper(TreeNode root){
        if (root == null){
            return;
        }
        list.add(root.val);
        helper(root.left);
        helper(root.right);
    }
}
