public class rotate_array {
    public void rotate(int[] nums, int k) {
        int N = nums.length;
        if(k>N){
            k=k%N;
        }
        rotateNums(nums, 0,N-1);
        rotateNums(nums, 0,k-1);
        rotateNums(nums, k,N-1);
    }
    public void rotateNums(int[] nums, int l, int r){
        while(l<r){
            int temp = nums[l];
            nums[l++] = nums[r];
            nums[r--] = temp;
            
        }
    }
}