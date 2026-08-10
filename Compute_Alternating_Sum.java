class Solution {
    public int alternatingSum(int[] nums) {
        int total = 0;
        for(int i = 0; i < nums.length; i++){
            total += Math.pow(-1,i) * nums[i];
        }
        return total;
    }
}
