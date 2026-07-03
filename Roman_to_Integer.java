class Solution {
    public int romanToInt(String s) {
        int result = 0;
        char[] characters = s.toCharArray();
        for(int i = 0; i < characters.length; i++){
            if(characters[i] == 'M'){
                result += 1000;
            }

            else if(characters[i] == 'D'){
                result += 500;
            }

            else if(characters[i] == 'C'){
                if(i+1 < characters.length){
                    if(characters[i+1] == 'D'){
                        result += 400;
                        i++;
                    }
                    else if(characters[i+1] == 'M'){
                        result += 900;
                        i++;
                    }
                    else{
                        result += 100;
                    }
                }
                else{
                    result += 100;
                }
            }

            else if(characters[i] == 'L'){
                result += 50;
            }

            else if(characters[i] == 'X'){
                if(i+1 < characters.length){
                    if(characters[i+1] == 'L'){
                        result += 40;
                        i++;
                    }
                    else if(characters[i+1] == 'C'){
                        result += 90;
                        i++;
                    }
                    else{
                        result += 10;
                    }
                    
                }
                else{
                    result += 10;
                }
            }

            else if(characters[i] == 'V'){
                result += 5;
            }

            else if(characters[i] == 'I'){
                if(i+1 < characters.length){
                    if(characters[i+1] == 'V'){
                        result += 4;
                        i++;
                    }
                    else if(characters[i+1] == 'X'){
                        result += 9;
                        i++;
                    }
                    else{
                        result += 1;
                    }
                }
                else{
                    result += 1;
                }
            }
        }
        return result;
    }
}
