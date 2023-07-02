public class find_peak_element {
    
}
class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length-1;
        while(l < r){
            int mid = (l+r)/2;
            if((mid-1)>-1 && nums[mid-1] < nums[mid] && (mid+1)<nums.length && nums[mid] > nums[mid+1]){
                return mid;
            }
            if(nums[mid] < nums[mid+1]){
                l = mid + 1;
            }
            else{
                r = mid - 1;
            }
        }
        return l;
    }
}