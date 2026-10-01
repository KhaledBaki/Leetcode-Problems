import java.util.Stack;
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        // Edge-Case where the length of the flower bed is 1
        if(flowerbed.length == 1 && n > 0){
            if (flowerbed[0] == 0){
                n--;
                return n == 0;
            }
        }
        
        // To Account for the "initial" previous value
        int prev = 0;
        for(int i = 0; i < flowerbed.length - 1; i++){
            if(prev == 1 || flowerbed[i + 1] == 1 || flowerbed[i] == 1){
                prev = flowerbed[i];
                continue;
            }
            if(prev == 0 && flowerbed[i + 1] == 0 && n > 0){
                flowerbed[i] = 1;
                prev = flowerbed[i];
                n--;
            }
        }

        // Edge-Case last two non reachable elements
        if(flowerbed.length >= 2 && n > 0 && flowerbed[flowerbed.length - 2] == 0 && flowerbed[flowerbed.length - 1] == 0){
            flowerbed[flowerbed.length - 1] = 0;
            n--;
        }
        return n == 0;
        
    }
}