public class min_cost_to_connect_all_points {
    
}
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int ptLen = points.length;
        if(ptLen == 0 || ptLen == 1){
            return 0;
        }
        Map<Integer, List<int[]>> adjMap = new HashMap<>();
        
        // Creating the adjacency dictionary
        for (int i = 0; i < ptLen; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < ptLen; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int cost = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                if (!adjMap.containsKey(i)) {
                    adjMap.put(i, new ArrayList<>());
                }
                if (!adjMap.containsKey(j)) {
                    adjMap.put(j, new ArrayList<>());
                }
                adjMap.get(i).add(new int[]{cost, j});
                adjMap.get(j).add(new int[]{cost, i});
            }
        }

        // Using PriorityQueue as MinHeap
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        Set<Integer> visited = new HashSet<>();
        int res = 0;
        
        minHeap.offer(new int[]{0, 0});

        // Dijkstra's Algorithm
        while (visited.size() < ptLen) {
            int[] pair = minHeap.poll();
            int cost = pair[0];
            int node1 = pair[1];
            
            if (visited.contains(node1)) {
                continue;
            }
            
            res += cost;
            visited.add(node1);
            
            for (int[] neighbor : adjMap.get(node1)) {
                int neiCost = neighbor[0];
                int nei = neighbor[1];
                if (!visited.contains(nei)) {
                    minHeap.offer(new int[]{neiCost, nei});
                }
            }
        }
        return res;
    }
}