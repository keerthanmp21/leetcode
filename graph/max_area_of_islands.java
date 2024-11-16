import java.util.*;

public class max_area_of_islands {
    
}

class Solution {
    private int ROWS;
    private int COLS;
    private int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private Set<String> visited = new HashSet<>();
    
    public int maxAreaOfIsland1(int[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        int maxSize = 0;
        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                maxSize = Math.max(maxSize, dfs(r, c, grid));
            }
        }
        return maxSize;
    }

    private int dfs(int r, int c, int[][] grid){
        if(r < 0 || r == ROWS || c < 0 || c == COLS || visited.contains(r + "," + c) || grid[r][c] == 0){
            return 0;
        }
        visited.add(r + "," + c);
        int size = 1;
        for(int[] d : directions){
            size += dfs(r + d[0], c + d[1], grid);
        }
        return size;
    }

    public int maxAreaOfIsland(int[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        int maxSize = 0;
        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                maxSize = Math.max(maxSize, dfs(r, c, grid));
            }
        }
        return maxSize;
    }

    private int bfs(int r, int c, int[][] grid){
        if(r < 0 || r == ROWS || c < 0 || c == COLS || visited.contains(r + "," + c) || grid[r][c] == 0){
            return 0;
        }
        Deque<int[]> deque = new LinkedList<>();
        deque.add(new int[]{r, c});
        int size = 1;

        while(!deque.isEmpty()){
            int[] cell = deque.poll();
            int row = cell[0];
            int col = cell[1];
            visited.add(r + "," + c);
            for(int[] d : directions){
                size += bfs(row + d[0], col + d[1], grid);
            }
        }

        return size;
    }
}