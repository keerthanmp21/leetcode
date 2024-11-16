import java.util.*;

public class course_schedule {
    
}

class Solution {
    private Map<Integer, List<Integer>> preMap;
    private Set<Integer> visitSet;

    public boolean canFinish1(int numCourses, int[][] prerequisites) {
        preMap = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            preMap.put(i, new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            int crs = prerequisite[0];
            int pre = prerequisite[1];
            preMap.get(crs).add(pre);
        }

        visitSet = new HashSet<>();  

        for (int crs = 0; crs < numCourses; crs++) {
            if (!dfs(crs)) {
                return false;
            }
        }

        return true;
    }

    public boolean dfs(int crs){
        if (visitSet.contains(crs)) {  
            return false;
        }
        if (preMap.get(crs).isEmpty()) {  
            return true;
        }
        visitSet.add(crs);
        for (int pre : preMap.get(crs)) {
            if (!dfs(pre)) {
                return false;
            }
        }
        visitSet.remove(crs);  
        preMap.put(crs, new ArrayList<>());  
        return true;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] preMap = new List[numCourses];
        int[] degrees = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            preMap[i] = new ArrayList<>();
        }

        for (int[] prerequisite : prerequisites) {
            int crs = prerequisite[0];
            int pre = prerequisite[1];
            preMap[pre].add(crs);
            degrees[crs]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int crs = 0; crs < numCourses; crs++) {
            if (degrees[crs] == 0) {
                queue.offer(crs);
            }
        }

        while (!queue.isEmpty()) {
            int crs = queue.poll();
            for (int nei : preMap[crs]) {
                degrees[nei]--;
                if (degrees[nei] == 0) {
                    queue.offer(nei);
                }
            }
        }

        for (int degree : degrees) {
            if (degree != 0) {
                return false;
            }
        }
        return true;
    }
}