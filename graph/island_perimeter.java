public class island_perimeter {
    
}
class Solution {
    public int islandPerimeter1(int[][] grid) {
        Set<String> visit = new HashSet<>();
        int row = 0, col = 0;
        for(int r = 0; r < grid.length; r++){
            for(int c = 0; c < grid[0].length; c++){
                if(grid[r][c] == 1){
                    row = r;
                    col = c;
                    break;
                }
            }
        }
        return dfs(grid, visit, row, col);
    }

    private int dfs(int[][] grid, Set<String> visit, int i, int j) {
        if (i >= grid.length || j >= grid[0].length || i < 0 || j < 0 || grid[i][j] == 0) {
            return 1;
        }
        if (visit.contains(i + "," + j)) {
            return 0;
        }
        visit.add(i + "," + j);
        int perim = dfs(grid, visit, i, j + 1);
        perim += dfs(grid, visit, i, j - 1);
        perim += dfs(grid, visit, i + 1, j);
        perim += dfs(grid, visit, i - 1, j);
        return perim;
    }

    private Set<int[]> visited = new HashSet<>();
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private int perims;
    private int ROWS;
    private int COLS;

    public int islandPerimeter(int[][] grid){
        ROWS = grid.length;
        COLS = grid[0].length;
        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if(grid[r][c] == 1 && !visited.contains(new int[]{r, c})){
                    bfs(r, c, grid);
                }
            }
        }

        return perims;

    }

    private void bfs(int row, int col, int[][] grid){
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{row, col});
        visited.add(new int[]{row, col});

        while(!q.isEmpty()){
            int[] cell = q.poll();
            int r = cell[0];
            int c = cell[1];
            for(int[] d : directions){
                int dr = r + d[0];
                int dc = c + d[1];
                if(dr < 0 || dr == ROWS || dc < 0 || dc == COLS){
                    perims++;
                }
                else if(grid[dr][dc] == 0){
                    perims++;
                }
                else if(grid[dr][dc] == 1 && !visited.contains(new int[]{dr, dc})){
                    visited.add(new int[]{dr, dc});
                    q.offer(new int[]{dr, dc});
                }
            }
        }
    }
}
