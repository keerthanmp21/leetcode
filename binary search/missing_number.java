import java.util.Arrays;
public class missing_number {
    
}

// greedy
// tc O(n), sc O(1)
class Solution1 {
    public int missingNumber(int[] nums) {
        
        int res = nums.length;
        for(int i = 0; i < nums.length; i++){
            res = res + i - nums[i];
        }
        return res;
        
    }
}

// binary search
// tc O(nlogn), sc O(n)
class Solution2 {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int l = 0, r = nums.length-1;
        while(l <= r){
            int mid = (l + r) / 2;
            if(nums[mid] == mid){
                l = mid + 1;
            }
            else{
                r = mid - 1;
            }
        }
        return l;
    }
}