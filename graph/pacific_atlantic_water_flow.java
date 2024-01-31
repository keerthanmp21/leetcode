class Solution {
    private int ROWS;
    private int COLS;
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    // dfs
    // tc O(m*n), sc O(m*n)
    public List<List<Integer>> pacificAtlantic1(int[][] heights) {
        ROWS = heights.length;
        COLS = heights[0].length;
        Set<String> pac = new HashSet<>();
        Set<String> atl = new HashSet<>();

        for(int c = 0; c < COLS; c++){
            dfs(0, c, pac, heights[0][c], heights);
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c], heights);
        }

        for(int r = 0; r < ROWS; r++){
            dfs(r, 0, pac, heights[r][0], heights);
            dfs(r, COLS - 1, atl, heights[r][COLS - 1], heights);
        }

        List<List<Integer>> res = new ArrayList<>();
        for(int r = 0; r < ROWS; r++){
            for(int c = 0; c < COLS; c++){
                if(pac.contains(r + "," + c) && atl.contains(r + "," + c)){
                    List<Integer> innerRes = new ArrayList();
                    innerRes.add(r);
                    innerRes.add(c);
                    res.add(innerRes);
                }
            }
        }

        return res;

    }

    private void dfs(int r, int c, Set<String> visited, int prevHeight, int[][] heights){
        if(visited.contains(r + "," + c) || r < 0 || r == ROWS || c < 0 || c == COLS || heights[r][c] < prevHeight){
            return;
        }
        visited.add(r + "," + c);
        dfs(r + 1, c, visited, heights[r][c], heights);
        dfs(r - 1, c, visited, heights[r][c], heights);
        dfs(r, c + 1, visited, heights[r][c], heights);
        dfs(r, c - 1, visited, heights[r][c], heights);
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int ROWS = heights.length;
        int COLS = heights[0].length;
        List<int[]> pacific = new ArrayList<>();
        List<int[]> atlantic = new ArrayList<>();
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int r = 0; r < ROWS; r++) {
            pacific.add(new int[]{r, 0});
            atlantic.add(new int[]{r, COLS - 1});
        }
        for (int c = 0; c < COLS; c++) {
            pacific.add(new int[]{0, c});
            atlantic.add(new int[]{ROWS - 1, c});
        }

        Set<int[]> pacificSet = bfs(pacific, heights, ROWS, COLS);
        Set<int[]> atlanticSet = bfs(atlantic, heights, ROWS, COLS);

        // Find common cells in both pacific and atlantic
        List<List<Integer>> res = new ArrayList<>();
        for (int[] cell : pacificSet) {
            if (atlanticSet.contains(cell)) {
                List<Integer> coordinate = new ArrayList<>();
                coordinate.add(cell[0]);
                coordinate.add(cell[1]);
                res.add(coordinate);
            }
        }
        return res;
    }

    public Set<int[]> bfs(List<int[]> l, int[][] heights, int ROWS, int COLS) {
        Queue<int[]> q = new ArrayDeque<>();
        Set<int[]> visit = new HashSet<>();
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int[] element : l) {
            q.offer(element);
            visit.add(element);
        }

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int r = current[0];
            int c = current[1];

            for (int[] dir : directions) {
                int dr = r + dir[0];
                int dc = c + dir[1];
                if (dr >= 0 && dr < ROWS && dc >= 0 && dc < COLS &&
                    !visit.contains(new int[]{dr, dc}) && heights[dr][dc] >= heights[r][c]) {
                    visit.add(new int[]{dr, dc});
                    q.offer(new int[]{dr, dc});
                }
            }
        }
        return visit;
    }
}