public class longest_subarray_of_1s_after_deleting_one_element {
    
}
class Solution {
    public int longestSubarray(int[] nums) {
        int l = 0, res = 0, k = 1;
        for(int r=0; r<nums.length;r++){
            if(nums[r]==0){
                k--;
            }
            while(k<0 && l<=r){
                if(nums[l]==0){
                    k++;
                }
                l++;
            }
            res = Math.max(res, r-l);
        }
        return res;
    }
}