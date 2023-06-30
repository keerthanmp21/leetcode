import java.util.*;
// two pointers and sorting
// tc O(nlogn+mlogm), sc O(n)
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int p1=0, p2=0;
        ArrayList<Integer> result = new ArrayList<Integer>();
        while(p1<nums1.length && p2<nums2.length){
            if(nums1[p1]<nums2[p2]){
                p1++;
            }
            else if(nums2[p2]<nums1[p1]){
                p2++;
            }
            else{
                result.add(nums1[p1]);
                p1++;
                p2++;
            }
        }
        int[] res= new int[result.size()];
        for(int i=0;i<result.size();i++){
            res[i] = result.get(i);
        }
        return res;
    }
}