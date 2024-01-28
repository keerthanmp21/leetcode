class Solution {
    private int ROWS, COLS;
    private final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private Set<String> visited = new HashSet<>();

    public int numIslands1(char[][] grid) {
        if(grid.length == 0 || grid[0].length == 0){
            return 0;
        }
        ROWS = grid.length;
        COLS = grid[0].length;
        int islands = 0;
        
        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if(grid[r][c] == '1' && !visited.contains(r + "-" + c)){
                    islands++;
                    dfs(grid, r, c);
                }
            }
        }

        return islands;

    }

    public void dfs(char[][] grid, int r, int c){
        if(r < 0 || r == ROWS || c < 0 || c == COLS || grid[r][c] != '1' || visited.contains(r + "-" + c)){
            return;
        }

        visited.add(r + "-" + c);
        for(int[] dir : directions){
            dfs(grid, r + dir[0], c + dir[1]);
        }

    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;
        Set<String> visited = new HashSet<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited.contains(r + "-" + c)) {
                    islands++;
                    bfs(grid, r, c, visited);
                }
            }
        }

        return islands;
    }

    private void bfs(char[][] grid, int r, int c, Set<String> visited) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c});
        visited.add(r + "-" + c);

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            for (int[] dir : directions) {
                int newRow = curr[0] + dir[0];
                int newCol = curr[1] + dir[1];
                if (newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol < grid[0].length && grid[newRow][newCol] == '1' && !visited.contains(newRow + "-" + newCol)) {
                    queue.offer(new int[]{newRow, newCol});
                    visited.add(newRow + "-" + newCol);
                }
            }
        }
    }
}