public class move_zeroes {
    public void moveZeroes(int[] nums) {
        int l = 0;
        for(int r = 1; r<nums.length;r++){
            if(nums[l] == 0 && nums[r] != 0){
                int temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
            }
            if(nums[l] != 0){
                l++;
            }
        }
    }
}