public class find_first_and_last_pos_of_element_in_sorted_array {
    
}
// tc O(logn), sc O(1)
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = getLeft(nums, target);
        int right = getRight(nums, target);
        if(left<=right){
            return new int[]{left, right};
        }
        return new int[]{-1,-1};
    }
    public int getLeft(int[] nums, int target){
        int l = 0 , r = nums.length-1;
        while(l<=r){
            int mid = (l+r)/2;
            if(target>nums[mid]){
                l = mid+1;
            }
            else{
                r = mid-1;
            }
        }
        return l;
    }
    public int getRight(int[] nums, int target){
        int l = 0 , r = nums.length-1;
        while(l<=r){
            int mid = (l+r)/2;
            if(target>=nums[mid]){
                l = mid+1;
            }
            else{
                r = mid-1;
            }
        }
        return r;
    }
}