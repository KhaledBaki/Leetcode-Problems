class Solution {
    public String addBinary(String a, String b) {

        boolean carry = false;

        // Converting string to chars
        char[] firstTerm = a.toCharArray();
        char[] secondTerm = b.toCharArray();

        String result = "";

        // subtracting one to accomodate array nature
        int i = firstTerm.length - 1;
        int j = secondTerm.length - 1;

        while(i >= 0 || j >= 0){
            
            
            char firstBit;
            if (i >= 0) {
                firstBit = firstTerm[i];
            }

            // Deals with length ambiguity
            else {
                firstBit = '0';
            }

            char secondBit;
            if (j >= 0) {
                secondBit = secondTerm[j];
            }

            // Deals with length ambiguity
            else {
                secondBit = '0';
            }

            if((firstBit == '1' && secondBit == '1') && carry == true){
                result = "1" + result;
                carry = true;
            }

            else if((firstBit == '1' && secondBit == '1') && carry == false){
                result = "0" + result;
                carry = true;
            }
           
            else if(((firstBit == '0' && secondBit == '1') || (firstBit == '1' && secondBit == '0')) && carry == false){
                result = "1" + result;
                carry = false;
            }

            else if(((firstBit == '0' && secondBit == '1') || (firstBit == '1' && secondBit == '0')) && carry == true){
                result = "0" + result;
                carry = true;
            }

            else if((firstBit == '0' && secondBit == '0') && carry == true){
                result = "1" + result;
                carry = false;
            }

            else if((firstBit == '0' && secondBit == '0') && carry == false){
                result = "0" + result;
                carry = false;
            }

            i--;
            j--;
        }

        // Adds 1 if there is a carry
        if(carry == true){
            result = "1" + result;
        }
        return result; 
    }
}
