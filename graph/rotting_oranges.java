public class rotting_oranges {
    
}

class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new ArrayDeque<>();
        int fresh = 0, time = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;

        // Finding fresh oranges and initializing the queue
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    fresh++;
                } else if (grid[r][c] == 2) {
                    q.offer(new int[]{r, c});
                }
            }
        }

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.isEmpty() && fresh > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] point = q.poll();
                int r = point[0];
                int c = point[1];
                for (int[] dir : directions) {
                    int row = r + dir[0];
                    int col = c + dir[1];
                    if (row < 0 || row >= ROWS || col < 0 || col >= COLS || grid[row][col] != 1) {
                        continue;
                    }
                    fresh--;
                    grid[row][col] = 2;
                    q.offer(new int[]{row, col});
                }
            }
            time++;
        }

        return fresh == 0 ? time : -1;
    }
}