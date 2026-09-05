class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int leftMax = nums[0];
        int[] prefixMax = new int[nums.length];

        int rightMin = nums[nums.length - 1];
        int[] suffixMin = new int[nums.length];

        for(int i = 0; i < nums.length; i++){
            // Prefix
            if (nums[i] > leftMax){
                prefixMax[i] = nums[i];
                leftMax = nums[i];
            } else {
                prefixMax[i] = leftMax;
            }

            // Suffix
            if (nums[nums.length - i - 1] < rightMin){
                suffixMin[nums.length - i - 1] = nums[nums.length - i - 1];
                rightMin = nums[nums.length - i - 1];
            } else {
                suffixMin[nums.length - i - 1] = rightMin;
            }
        }

        for(int i = 0; i < nums.length; i++){
            if (prefixMax[i] - suffixMin[i] <= k){
                return i;
            }
        }

        return -1;
    }
}
