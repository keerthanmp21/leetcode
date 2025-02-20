import java.util.*;

public class kth_largest_element_in_array {
    public static void main(String[] args) {
        
    }
}

class Solution {
    // heap(priority queue)
    // tc O(nlogk), sc O(1)
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        return minHeap.poll();
    }

    // sorting
    // tc O(nlogn), sc O(1)
    public int findKthLargest2(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}