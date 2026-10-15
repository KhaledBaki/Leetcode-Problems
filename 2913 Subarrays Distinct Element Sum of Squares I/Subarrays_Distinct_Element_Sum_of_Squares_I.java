class Solution {
    public int sumCounts(List<Integer> nums) {
        int sumOfSquares = 0;

        for(int i = 0; i < nums.size(); i++){
            List<Integer> current = new ArrayList<>();
            for(int j = i; j < nums.size(); j++){
                if(!current.contains(nums.get(j))){
                    current.add(nums.get(j));
                }
                sumOfSquares += current.size() * current.size();
            }
        }
        return sumOfSquares;
    }
}
