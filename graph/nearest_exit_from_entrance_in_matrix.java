import java.util.*;

public class nearest_exit_from_entrance_in_matrix {
    
}

class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int ROWS = maze.length;
        int COLS = maze[0].length;

        Queue<int[]> q = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        q.offer(entrance);
        visited.add(entrance[0] + "," + entrance[1]);

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        int steps = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cell = q.poll();
                int r = cell[0];
                int c = cell[1];
                if ((r == 0 || c == 0 || r == ROWS - 1 || c == COLS - 1) && (r != entrance[0] || c != entrance[1])) {
                    return steps;
                }
                for (int[] dir : directions) {
                    int row = r + dir[0];
                    int col = c + dir[1];
                    if (row >= 0 && row < ROWS && col >= 0 && col < COLS && maze[row][col] == '.' && !visited.contains(row + "," + col)) {
                        visited.add(row + "," + col);
                        q.offer(new int[]{row, col});
                    }
                }
            }
            steps++;
        }

        return -1;
    }
}