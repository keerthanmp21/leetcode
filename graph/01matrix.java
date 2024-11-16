import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int ROWS = mat.length;
        int COLS = mat[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int dist = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (mat[r][c] == 0) {
                    q.offer(new int[]{r, c});
                    visited.add(r + "," + c);
                }
            }
        }

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cell = q.poll();
                int r = cell[0];
                int c = cell[1];
                mat[r][c] = dist;
                for (int[] dir : directions) {
                    int dr = r + dir[0];
                    int dc = c + dir[1];
                    if (dr < 0 || dr == ROWS || dc < 0 || dc == COLS || visited.contains(dr + "," + dc) || mat[dr][dc] == 0) {
                        continue;
                    }
                    q.offer(new int[]{dr, dc});
                    visited.add(dr + "," + dc);
                }
            }
            dist++;
        }

        return mat;

    }
}