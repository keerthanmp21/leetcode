// two pointers
// tc O(n), sc O(1)
class Solution {
    public boolean isPalindrome(String s) {
        int l=0, r=s.length()-1;
        while(l<r){
            while(l<r &&  !isAlphaNumeric(s.charAt(l))){
                l++;
            }
            while(l<r && !isAlphaNumeric(s.charAt(r))){
                r--;
            }
            if(Character.toUpperCase(s.charAt(l)) != Character.toUpperCase(s.charAt(r))){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
    public boolean isAlphaNumeric(char c){
        //return Character.isLetterOrDigit(c);
        return (('a'<=c && c<='z') ||
        ('A'<=c && c<='Z') ||
        ('0'<=c && c<='9'));
    }
}