class Solution {
    public int snakesAndLadders(int[][] board) {
        int N = board.length;
        reverseBoard(board);
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{1, 0});
        Set<Integer> visited = new HashSet<>();

        while(!queue.isEmpty()){
            int[] val = queue.poll();
            int square = val[0];
            int moves = val[1];
            for(int i = 1; i < 7; i++){
                int nextSquare = square + i;
                int[] itp = intToPos(nextSquare, N);
                int r = itp[0];
                int c = itp[1];
                if(board[r][c] != -1){
                    nextSquare = board[r][c];
                }
                if(nextSquare == N * N){
                    return moves + 1;
                }
                if(!visited.contains(nextSquare)){
                    visited.add(nextSquare);
                    queue.add(new int[]{nextSquare, moves + 1});
                }
            }
        }
        return -1;
    }

    private void reverseBoard(int[][] board) {
        for (int i = 0; i < board.length / 2; i++) {
            int[] temp = board[i];
            board[i] = board[board.length - 1 - i];
            board[board.length - 1 - i] = temp;
        }
    }

    private int[] intToPos(int square, int N){
        int r = (square - 1) / N;
        int c = (square - 1) % N;
        if(r % 2 == 1){
            c = N - 1 - c;
        }
        return new int[]{r, c};
    }
}