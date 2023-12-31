// two pointers
// tc O(n), sc O(1)
public class two_sum2_input_array_sorted {
    public int[] twoSum(int[] numbers, int target) {
        int l=0, r=numbers.length-1;
        while(l<r){
            int curSum = numbers[l]+numbers[r];
            if(curSum<target){
                l++;
            }
            else if(curSum>target){
                r--;
            }
            else{
                return new int[]{++l, ++r};
            }
        }
        return new int[]{};
    }
}