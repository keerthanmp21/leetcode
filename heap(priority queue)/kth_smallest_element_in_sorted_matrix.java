import java.util.*;

public class kth_smallest_element_in_sorted_matrix {
    // maxheap
    // tc O(m*n*logk)
    public int kthSmallest(int[][] matrix, int k) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> Integer.compare(o2, o1));
        for(int r = 0; r<ROWS; r++){
            for(int c = 0; c<COLS; c++){
                maxHeap.offer(matrix[r][c]);
                if(maxHeap.size()>k){
                    maxHeap.poll();
                }
            }
        }

        return maxHeap.poll();
    }

    // minheap
    // tc O(k*logk), sc O(k)
    public int kthSmallest2(int[][] matrix, int k) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));

        for(int r=0; r<Math.min(ROWS, k); r++){
            minHeap.offer(new int[]{matrix[r][0], r, 0});
        }

        int res = -1;
        for(int i=0; i<k; i++){
            int[] poll_value = minHeap.poll();
            res = poll_value[0];
            int r = poll_value[1];
            int c = poll_value[2];
            if(c+1 < COLS){
                minHeap.offer(new int[]{matrix[r][c+1], r, c+1});
            }
        }

        return res;
    }
}
