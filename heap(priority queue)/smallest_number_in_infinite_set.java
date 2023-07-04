import java.util.PriorityQueue;;
public class smallest_number_in_infinite_set {
    private Integer minNum;
    private PriorityQueue<Integer> minHeap;
    public smallest_number_in_infinite_set() {
        minHeap = new PriorityQueue<>();
        minNum = 1;
    }
    
    public int popSmallest() {
        if(!minHeap.isEmpty()){
            return this.minHeap.poll();
        }
        int res = minNum;
        minNum++;
        return res;
    }
    
    public void addBack(int num) {
        if(num < minNum && !(minHeap.contains(num))){
            minHeap.offer(num);
        }
    }
}
