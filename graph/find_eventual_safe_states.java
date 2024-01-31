public class find_eventual_safe_states {
    
}

class Solution {
    // dfs
    public List<Integer> eventualSafeNodes1(int[][] graph) {
        Map<Integer, Boolean> safe = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < graph.length; i++){
            if(dfs(i, safe, graph)){
                res.add(i);
            }
        }
        return res;
    }

    private boolean dfs(int i, Map<Integer, Boolean> safe, int[][] graph){
        if(safe.containsKey(i)){
            return safe.get(i);
        }
        safe.put(i, false);
        for(int j = 0; j < graph[i].length; j++){
            int nei = graph[i][j];
            if(!dfs(nei, safe, graph)){
                return safe.get(nei);
            }
        }
        safe.put(i, true);
        return true;
    }

    // bfs
    public List<Integer> eventualSafeNodes2(int[][] graph){
        int N = graph.length;
        List<List<Integer>> edges = new ArrayList<>(N);
        for(int i = 0; i < N; i++){
            edges.add(new ArrayList());
        }
        int[] indegree = new int[N];
        for(int i = 0; i < N; i++){
            indegree[i] = graph[i].length;
            for (int j : graph[i]) {
                edges.get(j).add(i);
            }
        }

        Deque<Integer> queue = new ArrayDeque<>();
        List<Integer> res = new ArrayList<>();

        for(int i = 0; i < N; i++){
            if(indegree[i] == 0){
                queue.add(i);
            }
        }

        while(!queue.isEmpty()){
            int u = queue.poll();
            res.add(u);
            for (int i : edges.get(u)) {
                if (indegree[i] != 0) {
                    indegree[i]--;
                    if (indegree[i] == 0) {
                        queue.add(i);
                    }
                }
            }
        }

        Collections.sort(res);
        return res;
    }
}