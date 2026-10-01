class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int i=0;
        int[] splitUp = new int[String.valueOf(x).length()];
        while(x > 0){
            splitUp[i] = x % 10;
            x /= 10;
            i++;
        }

        for(int j = 0; j < splitUp.length ; j++){
            if(splitUp[j] != splitUp[splitUp.length - j - 1]){
                return false;
            }
        }
        return true;
    }
}
