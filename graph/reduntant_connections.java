public class reduntant_connections {
    
}
class Solution {
    // union find
    // time O(n), space O(n)
    public int[] findRedundantConnection(int[][] edges) {
        int N = edges.length;
        int[] parent = new int[N + 1];
        int[] weight = new int[N + 1];
        for(int i = 0; i < N; i++){
            parent[i] = i;
            weight[i] = 1;
        }
        // or Array.fill(weight, 1)

        for(int[] edg : edges){
            int n1 = edg[0];
            int n2 = edg[1];
            if(!union(n1, n2, parent, weight)){
                return edg;
            }
        }
        return new int[]{-1, -1};

    }

    private int find(int n, int[] parent){
        int p = parent[n];
        while(p != parent[p]){
            p = parent[p];
        }
        return p;
    }

    private boolean union(int n1, int n2, int[] parent, int[] weight){
        int p1 = find(n1, parent);
        int p2 = find(n2, parent);

        if(p1 == p2){
            return false;
        }
        if(weight[p2] > weight[p1]){
            parent[p1] = p2;
            weight[p2] = weight[p2] + weight[p1];
        }
        else{
            parent[p2] = p1;
            weight[p1] = weight[p1] + weight[p2];
        }
        return true;
    }

    // dfs
    // time O(n^2), space O(n^2)
    public int[] findRedundantConnection2(int[][] edges){
        int N = edges.length;
        Map<Integer, List<Integer>> edgesList = new HashMap<>();

        for(int i = 0; i < N + 1; i++){
            edgesList.put(i, new ArrayList());
        }

        for(int[] edg : edges){
            int src = edg[0];
            int dest = edg[1];
            Set<Integer> visitSet = new HashSet<>();
            if(dfs(src, dest, edgesList, visitSet)){
                return edg;
            }
            edgesList.get(src).add(dest);
            edgesList.get(dest).add(src);
        }

        return new int[]{-1, -1};

    }

    private boolean dfs(int src, int dest, Map<Integer, List<Integer>> edgesList, Set<Integer> visitSet){
        if(visitSet.contains(src)){
            return false;
        }
        if(src == dest){
            return true;
        }
        visitSet.add(src);
        List<Integer> curList = edgesList.get(src);
        for(int i = 0; i < curList.size(); i++){
            int node = curList.get(i);
            if(dfs(node, dest, edgesList, visitSet)){
                return true;
            }
        }
        return false;
    }

    public int[] findRedundantConnection3(int[][] edges){
        int N = edges.length;
        Map<Integer, List<Integer>> edgesList = new HashMap<>();

        for(int i = 0; i < N + 1; i++){
            edgesList.put(i, new ArrayList());
        }

        for(int[] edg : edges){
            int src = edg[0];
            int dest = edg[1];
            Set<Integer> visitSet = new HashSet<>();
            if(bfs(src, dest, edgesList, visitSet)){
                return edg;
            }
            edgesList.get(src).add(dest);
            edgesList.get(dest).add(src);
        }

        return new int[]{-1, -1};

    }

    // bfs
    // time O(n^2), space O(n^2)
    private boolean bfs(int src, int dest, Map<Integer, List<Integer>> edgesList, Set<Integer> visitSet){
        Deque<Integer> deque = new ArrayDeque<>();
        deque.offer(src);
        visitSet.add(src);
        while(!deque.isEmpty()){
            int curNode = deque.poll();
            if(curNode == dest){
                return true;
            }
            List<Integer> curList = edgesList.get(curNode);
            for(int i = 0; i < curList.size(); i++){
                int neiNode =curList.get(i);
                if(!visitSet.contains(neiNode)){
                    visitSet.add(neiNode);
                    deque.offer(neiNode);
                }
            }
        }
        return false;
    }
}