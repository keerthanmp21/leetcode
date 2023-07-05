import java.util.PriorityQueue;

public class total_cost_to_hire_k_workers {
    public long totalCost(int[] costs, int k, int candidates) {
        int i = 0, j = costs.length-1;
        long res = 0;
        PriorityQueue<Integer> first_candidates = new PriorityQueue<>();
        PriorityQueue<Integer> last_candidates = new PriorityQueue<>();
        
        while(k > 0){
            while(first_candidates.size() < candidates && i <= j){
                first_candidates.add(costs[i++]);
            }
            while(last_candidates.size() < candidates && i <= j){
                last_candidates.add(costs[j--]);
            }

            
            int first_value = first_candidates.size()>0 ? first_candidates.peek() : Integer.MAX_VALUE;
            int last_value = last_candidates.size()>0 ? last_candidates.peek() : Integer.MAX_VALUE;            

            if(first_value <= last_value){
                res = res + first_value;
                first_candidates.poll();
            }
            else{
                res = res + last_value;
                last_candidates.poll();
            }
            k--;
        }
        return res;
    }
}
