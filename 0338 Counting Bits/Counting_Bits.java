class Solution {
    public int[] countBits(int n) {
        int[] container = new int[n + 1];

        for(int i = 0; i < n + 1; i++){
            
            // makes sure the first entry is always zero
            if(i == 0){
                container[i] = 0;
                continue;
            }

            // to itterate from position i
            int subNumber = i;

            // counter resets as we go up in sub numbers
            int counter = 0;

            // itterate over specific sub number
            while(subNumber > 0){
                if(subNumber % 2 != 0){
                    counter++;
                }
                subNumber = subNumber / 2;
            }

            // store value for the sub number
            container[i] = counter;
        }

        // return int[] object
        return container;
    }
}
