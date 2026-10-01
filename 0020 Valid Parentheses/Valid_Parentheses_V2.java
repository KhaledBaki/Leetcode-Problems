import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        String open = "{([";
        String close = "})]";

        char[] c = s.toCharArray();

        for (int i = 0; i < c.length; i++){
            if (open.indexOf(c[i]) != -1){
                stack.push(c[i]);
            }
            else if (close.indexOf(c[i]) != -1){
                if (stack.isEmpty()){
                    return false;
                }
                if (open.indexOf(stack.pop()) != close.indexOf(c[i])){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
