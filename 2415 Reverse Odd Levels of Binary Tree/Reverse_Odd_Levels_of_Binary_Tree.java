import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {

        // Queue is used for the BFS Algorithm
        Queue<TreeNode> queue = new LinkedList<>();

        // Array is reserved for reversing at a specific depth
        List<TreeNode> list = new ArrayList<>();

        // height for the perfect binary tree
        int height = perfectTreeHeight(root);
        
        // initial condition for the BFS
        queue.add(root);

        // Outer loop goes height by height
        for(int i = 0; i < height; i++){

            // inner for loop completes the BFS algorithm 
            int size = queue.size();
            for(int j = 0; j < size; j++){
                TreeNode node = queue.remove();

                if (node == null)
                    continue;
                queue.add(node.left);
                queue.add(node.right);

                if(i % 2 != 0){
                    list.add(node);
                }
                
            }
            if(i % 2 != 0){
                for(int k = 0; k < list.size() / 2; k++){

                    int temp = list.get(k).val;
                    list.get(k).val = list.get(list.size() - k - 1).val;
                    list.get(list.size() - k - 1).val = temp;
                
                }
                list.clear();
            }
        }
        return root;
    }

    public int perfectTreeHeight(TreeNode root){
        int height = 0;
        TreeNode cursor = root;
        while(cursor != null){
            cursor = cursor.right;
            height++; 
        }
        return height;
    }
}
