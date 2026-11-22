class Solution {
    public boolean checkString(String s) {
        char[] c = s.toCharArray();
        boolean firstA = false;

        for(char ch : c){
            
            if (ch == 'b' && !firstA){
                firstA = true;
            }
            else if (ch == 'a' && firstA){
                return false;
            }
        }
        return true;
    }
}
