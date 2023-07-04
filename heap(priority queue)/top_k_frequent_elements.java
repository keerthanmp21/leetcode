import java.util.*;
public class top_k_frequent_elements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numOfOccurences = new HashMap<>();
        for(int n:nums){
            numOfOccurences.put(n, numOfOccurences.getOrDefault(n,0)+1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = 
                         new PriorityQueue<>((a,b)->(b.getValue()-a.getValue()));
        for(Map.Entry<Integer,Integer> entry: numOfOccurences.entrySet()){
            maxHeap.add(entry);
        }
        List<Integer> res = new ArrayList<>();
        for(int i=0; i<k; i++){
            Map.Entry<Integer, Integer> entry = maxHeap.poll();
            res.add(entry.getKey());
        }
        return res.stream().mapToInt(Integer::intValue).toArray();

    }
}
