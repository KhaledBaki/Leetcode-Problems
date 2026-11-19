import java.util.Stack;
import java.util.LinkedList;

class Solution {
    public String reverseVowels(String s) {
        String vowelLetters = "aeiou";
        char[] chars = s.toCharArray();
        Stack<Character> vowels = new Stack<>();
        for (int i = 0; i < s.length(); i++){

            char c = Character.toLowerCase(chars[i]);
            char original = chars[i];

            if(vowelLetters.indexOf(c) != -1){
                vowels.push(original);
            }
        }
        for (int i = 0; i < s.length(); i++){
            char c = Character.toLowerCase(chars[i]);
            if(vowelLetters.indexOf(c) != -1){
                chars[i] = vowels.pop();
            }
        }
        String str1 = new String(chars);
        return str1;
    }
}
