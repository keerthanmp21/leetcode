public class max_no_of_vowels_in_substring_of_given_length {
    
}
// tc O(n), sc O(1)
class Solution {
    public int maxVowels(String s, int k) {
        int l=0, res=0, numOfVowels=0;
        for(int r=0;r<s.length();r++){
            if("aeiou".indexOf(s.charAt(r))!=-1){
                numOfVowels++;
            }
            if((r-l+1)==k){
                res = Math.max(res, numOfVowels);
                if("aeiou".indexOf(s.charAt(l))!=-1){
                    numOfVowels--;
                }
                l++;
            }
        }
        return res;
    }
}
