import java.util.*;
public class kth_largest_element_in_array {
    
}

// minheap
// tc O(nlogk), sc O(1)
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        for(int num:nums){
            minHeap.add(num);
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }
        return minHeap.poll();
    }
}

// maxheap
// tc O(nlogn), sc O(1)
class Solution2 {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int num:nums){
            maxHeap.add(num);
        }
        for(int i = 0;i < k-1; i++){
            maxHeap.poll();
        }
        return maxHeap.poll();
    }
}