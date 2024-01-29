public class Solution {
    public int[] findOrder1(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> prereq = new HashMap<>();
        for(int i = 0; i < numCourses; i++){
            prereq.put(i, new ArrayList<>());
        }
        for (int[] pair : prerequisites) {
            prereq.get(pair[0]).add(pair[1]);
        }

        List<Integer> output = new ArrayList();
        Set<Integer> cycle = new HashSet<>();
        Set<Integer> visit = new HashSet<>();

        for(int c = 0; c < numCourses; c++){
            if(!dfs(c, cycle, visit, prereq, output)){
                return new int[]{};
            }
        }

        int[] outputArr = new int[output.size()];
        for(int i = 0; i < output.size(); i++){
            outputArr[i] = output.get(i);
        }

        return outputArr;

    }

    public boolean dfs(int crs, Set<Integer> cycle, Set<Integer> visit, Map<Integer, List<Integer>> prereq, List output){
        if(cycle.contains(crs)){
            return false;
        }
        if(visit.contains(crs)){
            return true;
        }
        cycle.add(crs);
        for(int pre : prereq.get(crs)){
            if(!dfs(pre, cycle, visit, prereq, output)){
                return false;
            }
        }
        cycle.remove(crs);
        visit.add(crs);
        output.add(crs);
        return true;
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> edges = new ArrayList<>();
        for(int i = 0; i < numCourses; i++){
            edges.add(new ArrayList<>());
        }
        int[] degrees = new int[numCourses];
        List<Integer> output = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            edges.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            int cur = prerequisite[0];
            int preCur = prerequisite[1];
            edges.get(preCur).add(cur);
            degrees[cur]++;
        }

        for (int i = 0; i < numCourses; i++) {
            if (degrees[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int cur = q.poll();
            output.add(cur);
            for (int preCur : edges.get(cur)) {
                degrees[preCur]--;
                if (degrees[preCur] == 0) {
                    q.offer(preCur);
                }
            }
        }

        if (output.size() == numCourses) {
            int[] result = new int[numCourses];
            for (int i = 0; i < numCourses; i++) {
                result[i] = output.get(i);
            }
            return result;
        } else {
            return new int[]{};
        }
    }
}
