import java.util.Arrays;


public class merge_sorted_array {
    //brute force
    // tc O(nlogn), sc O(n)
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i=0;i<n;i++){
            nums1[m+i] = nums2[i];
        }
        Arrays.sort(nums1);
    }

    //two pointers
    // tc O(n), sc O(n)
    public void merge2(int[] nums1, int m, int[] nums2, int n) {
        int l=m-1, r=m+n-1, i=n-1;
        while(i>=0){
            if(l>=0 && nums1[l]>nums2[i]){
                nums1[r] = nums1[l--];
            }
            else{
                nums1[r] = nums2[i--];
            }
            r--;
        }

    }
}