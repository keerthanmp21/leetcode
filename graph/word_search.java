import java.util.Set;
import java.util.HashSet;

public class word_search {
    
}

class Solution {
    private int ROWS, COLS;
    private Set<String> path;
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public boolean exist(char[][] board, String word) {
        ROWS = board.length;
        COLS = board[0].length;
        path = new HashSet<>();
        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if(dfs(board, r, c, word, 0)){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, int r, int c, String word, int i){
        if(i == word.length()){
            return true;
        }
        if(r < 0 || c < 0 || r == ROWS || c == COLS || word.charAt(i) != board[r][c] || path.contains(r + "," + c)){
            return false;
        }
        path.add(r + "," + c);
        boolean res = false;
        for(int[] dir : directions){
            res = res || dfs(board, r + dir[0], c + dir[1], word, i + 1);
        }
        path.remove(r + "," + c);
        return res;
    }
}