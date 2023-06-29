class Solution {
    public int strStr(String haystack, String needle) {
        int l1=0, l2=0, r1=haystack.length(), r2=needle.length();
        while(l1<r1){
            if(l2==r2){
                return l1-l2;
            }
            if(haystack.charAt(l1) == needle.charAt(l2)){
                l2++;
            }
            else{
                l1 = l1-l2;
                l2 = 0;
            }
            l1++;
        }
        if(l2==r2){
            return l1-l2;
        }
        return -1;
    }
}