public class max_consecutives_ones3 {
    
}
// tc O(n), sc O(1)
class Solution {
    public int longestOnes(int[] nums, int k) {
        int l=0, r=0, cur_count=0, res=0;
        while(r<nums.length){
            if(nums[r]==1){
                r++;
                cur_count++;
            }
            else if(nums[r]==0 && k>0){
                k--;
                cur_count++;
                r++;
            }
            else{
                res=Math.max(res,cur_count);
                while(nums[l]==1){
                    l++;
                }
                l++;
                r++;
                cur_count=r-l;
            }
        }
        return Math.max(res,cur_count);
    }
}