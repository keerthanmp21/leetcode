import java.util.HashSet;

public class longest_substring_without_repeating_characters {
    
}

// sliding window
// tc O(n), sc O(n)
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> charSet = new HashSet<Character>();
        int l = 0, res = 0;
        for(int r=0; r<s.length(); r++){
            while(charSet.contains(s.charAt(r))){
                charSet.remove(s.charAt(l++));
            }
            charSet.add(s.charAt(r));
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}