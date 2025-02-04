import java.util.*;

public class surrounded_regions {
    
}

class Solution {
    private int ROWS, COLS;
    private final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void solve1(char[][] board) {
        ROWS = board.length;
        COLS = board[0].length;

        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if((r == 0 || r == ROWS - 1 || c == 0 || c == COLS - 1) && board[r][c] == 'O'){
                    dfs(board, r, c);
                }
            }
        }

        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if(board[r][c] == 'O'){
                    board[r][c] = 'X';
                }
                if(board[r][c] == 'T'){
                    board[r][c] = 'O';
                }
            }
        }

    }

    public void dfs(char[][] board, int r, int c){
        if(r < 0 || c < 0 || r == ROWS || c == COLS || board[r][c] != 'O'){
            return;
        }
        board[r][c] = 'T';
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }

    public void solve2(char[][] board) {
        ROWS = board.length;
        COLS = board[0].length;
        Queue<int[]> queue = new ArrayDeque<>();

        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if((r == 0 || r == ROWS - 1 || c == 0 || c == COLS - 1) && board[r][c] == 'O'){
                    queue.offer(new int[]{r, c});
                }
            }
        }

        while(!queue.isEmpty()){
            int[] point = queue.poll();
            int r = point[0];
            int c = point[1];
            if (r < 0 || r >= ROWS || c < 0 || c >= COLS || board[r][c] != 'O') continue;

            board[r][c] = 'T'; // Mark as 'T' for temporarily safe

            for (int[] dir : directions) {
                int newRow = r + dir[0];
                int newCol = c + dir[1];
                queue.offer(new int[]{newRow, newCol});
            }
        }

        // Convert remaining 'O's to 'X's and restore 'T's back to 'O's
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                if (board[r][c] == 'T') board[r][c] = 'O';
            }
        }

    }
}