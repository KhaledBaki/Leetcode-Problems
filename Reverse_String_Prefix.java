import java.util.Stack;
class Solution {
    public String reversePrefix(String s, int k) {
        Stack<Character> stack = new Stack<Character>();
        String newWord = "";
        char[] c = s.toCharArray();

        for(int i = 0; i < k; i++){
            stack.push(c[i]);
        }

        while(!stack.isEmpty()){
            newWord += stack.pop();
        }
        
        for(int i = k; i < c.length; i++){
            newWord += c[i];
        }
        
        return newWord;
    }
}
