import java.util.HashSet;
import java.util.Set;

class Solution {

    // NOTE: not solved yet, will solve later with DFS algorithm!
    // This set keeps track of nodes we visit
    private Set<Integer> goodNodesSet = new HashSet<>();

    // total number of goodNodes
    int total = 0;

    // used for the first helper method call
    boolean first2 = false;
    public int goodNodes(TreeNode root) {

        if(!first2){
            helper(root, -1);
        }
        if (root == null){
            return;
        }
        goodNodes(root.left);
        if(goodNodesSet.contains(root.val)){
            total++;
        }
        goodNodes(root.right);
        first = true;
        return total;
    }

    private boolean first = true;
    private void helper(TreeNode root, int prev){
        if(root == null){
            return;
        }

        if (first){
            goodNodesSet.add(root.val);
            first = false;
        }

        if(root.val > prev){
            helper(root.left, root.val);
            goodNodesSet.add(root.val);
            helper(root.right, root.val);
        }
    }
}
