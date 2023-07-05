import java.util.Arrays;
import java.util.PriorityQueue;

public class max_subsequence_score {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int N = nums1.length;
        int[][] pairs = new int[N][2];
        for(int i=0;i<N;i++){
            pairs[i] = new int[]{nums2[i], nums1[i]};
        }
        Arrays.sort(pairs,(a,b)->b[0]-a[0]);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k,(a,b)->a-b);
        long res = 0, total = 0;
        for(int[] pair:pairs){
            minHeap.add(pair[1]);
            total = total + pair[1];
            if(minHeap.size()>k){
                total = total - minHeap.poll();
            }
            if(minHeap.size() == k){
                res = Math.max(res, total*pair[0]);
            }
        }
        return res;
    }
}
