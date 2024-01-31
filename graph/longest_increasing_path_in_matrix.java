public class longest_increasing_path_in_matrix {
    
}

class Solution {
    // dfs
    // tc O(m*n), sc O(m*n)
    private int ROWS;
    private int COLS;
    private int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private int maxValue = 0;
    private Map<String, Integer> cache;

    public int longestIncreasingPath(int[][] matrix) {
        ROWS = matrix.length;
        COLS = matrix[0].length;
        cache = new HashMap<>();

        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                dfs(r, c, -1, matrix);
            }
        }

        return maxValue;

    }

    private int dfs(int r, int c, int preValue, int[][] matrix){
        if(r < 0 || c < 0 || r == ROWS || c == COLS || matrix[r][c] <= preValue){
            return 0;
        }
        if(cache.containsKey(r + "," + c)){
            return cache.get(r + "," + c);
        }
        int res = 1;
        for(int[] d : directions){
            res = Math.max(res, 1 + dfs(r + d[0], c + d[1], matrix[r][c], matrix));
        }
        cache.put(r + "," + c, res);
        maxValue = Math.max(maxValue, res);
        return res;
    }
}