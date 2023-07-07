import java.util.Arrays;


public class sort_colors {
    // sorting
    // tc O(nlogn), sc O(1)
    public void sortColors(int[] nums) {
        Arrays.sort(nums);
    }

    //count sort
    // tc O(n), sc O(3)
    public void sortColors2(int[] nums) {
        int[] sort = new int[3];
        for(int i=0; i<nums.length;i++){
            sort[nums[i]]++;
        }
        int pt = 0;
        for(int i=0;i<3;i++){
            for(int j=0;j<sort[i];j++){
                nums[pt++] = i;
            }
        }
    }

    // two pointers
    // tc O(n), sc O(n)
    public void sortColors3(int[] nums) {
        int i=0, l=0, r=nums.length-1;
        while(i<=r){
            if(nums[i]==0){
                nums[i++] = nums[l];
                nums[l++] = 0;
                
            }
            else if(nums[i] == 1){
                i++;
            }
            else{
                nums[i] = nums[r];
                nums[r--] = 2;
            }
        }
    }
}