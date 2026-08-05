import java.util.Stack;
class Solution {
    public boolean isPowerOfTwo(int n) {
        Stack<Integer> stack = new Stack<Integer>();
        int counter = 0;
        while(n > 0){
            stack.push(n % 2);
            n /= 2;
        }
        
        while(!stack.isEmpty()){
            if(stack.pop() == 1){
                counter++;
            }
        }
        if(counter == 1){
            return true;
        }
        else{
            return false;
        }
    }
}
