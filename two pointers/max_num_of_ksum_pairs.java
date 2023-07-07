import java.util.Arrays;
// two pointers and sorting
// tc O(nlogn), sc O(1)
public class max_num_of_ksum_pairs {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int l=0, r=nums.length-1, total_count=0;
        while(l<r){
            int curSum = nums[l]+nums[r];
            if(curSum<k){
                l++;
            }
            else if(curSum>k){
                r--;
            }
            else{
                total_count++;
                l++;
                r--;
            }
        }
        return total_count;
    }
}