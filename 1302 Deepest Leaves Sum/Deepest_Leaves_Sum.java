import java.util.Queue;
import java.util.LinkedList;
class Solution {
    public int deepestLeavesSum(TreeNode root) {

        int sum = 0;
        int height = height(root);
        Queue<TreeNode> queue = new LinkedList<>();
        
        queue.add(root);
        for (int i = 0; i < height - 1; i++){
            int size = queue.size();
            for(int j = 0; j < size; j++){
                TreeNode node = queue.remove();
                if (node.left != null)
                    queue.add(node.left);
                
                if (node.right != null)
                    queue.add(node.right);
            }
        }
        int size = queue.size();
        for (int i = 0; i < size; i++){
            sum += queue.remove().val;
        }
        return sum;
    }
    public int height(TreeNode root){
        if (root == null){
            return 0;
        }
        return Math.max(height(root.left), height(root.right)) + 1;
    }
}
