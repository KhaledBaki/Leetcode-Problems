import java.util.Stack;
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null){
            return true;
        }

        Stack<TreeNode> stack = new Stack<>();
        
        // First case
        stack.push(root.left);
        stack.push(root.right);

        // Breadth First Search algorithm
        while(!stack.isEmpty()){
            
            // left tree
            TreeNode e1 = stack.pop();
            TreeNode e2 = stack.pop();

            if(e1 == null && e2 == null){

                // goes to the next step and goes to the next iteration
                continue;
            }
            if(e1 == null || e2 == null || e1.val != e2.val){
                return false;
            }
            stack.push(e1.left);
            stack.push(e2.right);
            
            stack.push(e1.right);
            stack.push(e2.left);
        }
        return true;
    }
}
