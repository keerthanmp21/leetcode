public class maximum_average_subarray1 {
    
}
// sliding window
// tc O(n), sc O(1)
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int l=0, res=Integer.MIN_VALUE, total=0;
        for(int r=0; r<nums.length;r++){
            if(r<k){
                total = total+nums[r];
            }
            else{
                res=Math.max(res,total);
                total = total-nums[l++]+nums[r];
            }
        }
        res=Math.max(res,total);
        return (double)res/k;
    }
}