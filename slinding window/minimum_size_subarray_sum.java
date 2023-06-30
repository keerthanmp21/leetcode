public class minimum_size_subarray_sum {
    
}
// sliding window
// tc O(n), sc O(1)
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0, res=Integer.MAX_VALUE, total=0;
        for(int r=0;r<nums.length;r++){
            total = total+nums[r];
            while(total>=target){
                res = Math.min(res, r-l+1);
                total = total-nums[l++];
            }
        }
        if(res==Integer.MAX_VALUE){
            return 0;
        }
        else{
            return res;
        }
    }
}
