class Solution {
    public String triangleType(int[] nums) {
        // Case 1: Not a triangle
        if(!(nums[0] + nums[1] > nums[2]) || !(nums[0] + nums[2] > nums[1]) || !(nums[1] + nums[2] > nums[0]))
            return "none";
        
        // Case 2: Equilateral triangle
        if(nums[0] == nums[1] && nums[1] == nums[2])
            return "equilateral";
        
        // Case 3: Isosceles triangle
        if(nums[0] == nums[1] || nums[0] == nums[2] || nums[1] == nums[2])
            return "isosceles";
            
        // Case 4: Scalene triangle
        return "scalene";
    }
}
