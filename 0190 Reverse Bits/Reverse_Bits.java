import java.util.Stack;
class Solution {
    public int reverseBits(int n) {
        Stack<Integer> stack1 = new Stack<Integer>();
        
        int result =  0;
        int i = 0;

        while(n > 0){
            stack1.push(n % 2);
            n /= 2;
        }
        
        while(stack1.size() < 32){
            stack1.push(0);
        }
        
        while(!stack1.isEmpty()){
            
            result += stack1.pop() * Math.pow(2 , i);
            i++;
        }

        return result;
    }
}
