public class shortest_bridge {
    
}
class Solution {
    public int shortestBridge(int[][] grid) {
        int N = grid.length;
        int[][] direct = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        Set<String> visit = new HashSet<>();
        
        // Depth First Search to mark one island cells
        Deque<int[]> queue = new ArrayDeque<>();
        
        // DFS function to mark one island cells
        // and put them into the visit set
        // We assume all cells are not visited yet.
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (grid[r][c] == 1) {
                    dfs(grid, r, c, visit);
                    return bfs(grid, direct, visit);
                }
            }
        }
        return -1; // No solution found
    }
    
    // Depth First Search to mark one island cells
    private void dfs(int[][] grid, int r, int c, Set<String> visit) {
        int N = grid.length;
        if (r < 0 || c < 0 || r >= N || c >= N || grid[r][c] == 0 || visit.contains(r + "-" + c))
            return;
        
        visit.add(r + "-" + c);
        
        for (int[] dir : new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
            dfs(grid, r + dir[0], c + dir[1], visit);
        }
    }
    
    // Breadth First Search to find the shortest bridge
    private int bfs(int[][] grid, int[][] direct, Set<String> visit) {
        int N = grid.length;
        Deque<int[]> queue = new ArrayDeque<>(visit.stream().map(s -> {
            String[] parts = s.split("-");
            return new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])};
        }).collect(Collectors.toList()));
        
        int res = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                int r = cell[0];
                int c = cell[1];
                for (int[] dir : direct) {
                    int newRow = r + dir[0];
                    int newCol = c + dir[1];
                    if (newRow < 0 || newRow >= N || newCol < 0 || newCol >= N || visit.contains(newRow + "-" + newCol))
                        continue;
                    
                    if (grid[newRow][newCol] == 1)
                        return res;
                    
                    queue.offer(new int[]{newRow, newCol});
                    visit.add(newRow + "-" + newCol);
                }
            }
            res++;
        }
        return -1; // No solution found
    }
}