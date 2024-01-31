public class reorder_routes_to_make_all_paths_lead_to_the_city_zero {
    
}

class Solution {
    private int result;
    public int minReorder1(int n, int[][] connections) {
        Set<String> edges = new HashSet<>();
        List<Integer>[] neighbors = new List[n];
        for (int i = 0; i < n; i++) {
            neighbors[i] = new ArrayList<>();
        }
        
        for (int[] connection : connections) {
            int a = connection[0];
            int b = connection[1];
            edges.add(a + "," + b);
            neighbors[a].add(b);
            neighbors[b].add(a);
        }
        
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        int[] changes = new int[]{0};

        result = 0;
        dfs(0, neighbors, edges, visited);
        return result;
    }

    private void dfs(int city, List<Integer>[] neighbors, Set<String> edges, Set<Integer> visited) {
        for (int nei : neighbors[city]) {
            if (visited.contains(nei)) {
                continue;
            }
            if (!edges.contains(nei + "," + city)) {
                result++;
            }
            visited.add(nei);
            dfs(nei, neighbors, edges, visited);
        }
    }

    public int minReorder(int n, int[][] connections){
        Map<Integer, List<int[]>> edges = new HashMap<>();
        for(int[] con : connections){
            int src = con[0];
            int dest = con[1];
            edges.putIfAbsent(src, new ArrayList());
            edges.putIfAbsent(dest, new ArrayList());
            edges.get(src).add(new int[]{dest, 1});
            edges.get(dest).add(new int[]{src, 0});
        }

        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(0);
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        int result = 0;

        while(!deque.isEmpty()){
            int curr = deque.poll();
            List<int[]> neighbors = edges.get(curr);
            for (int[] neighbor : neighbors) {
                int neiCity = neighbor[0];
                int cost = neighbor[1];
                if(!visited.contains(neiCity)){
                    visited.add(neiCity);
                    deque.add(neiCity);
                    result += cost;
                }
            }
        }

        return result;

    }
}