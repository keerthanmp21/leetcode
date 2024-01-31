class Solution {
    public int swimInWater(int[][] grid) {
        int N = grid.length;
        PriorityQueue<int[]> minH = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        minH.offer(new int[]{grid[0][0], 0, 0});
        Set<String> visited = new HashSet<>();
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while(!minH.isEmpty()){
            int[] val = minH.poll();
            int t = val[0];
            int r = val[1];
            int c = val[2];
            if(r == N - 1 && c == N - 1){
                return t;
            }
            for(int[] d : directions){
                int neiR = r + d[0];
                int neiC = c + d[1];
                if(neiR < 0 || neiR == N || neiC < 0 || neiC == N || visited.contains(neiR + "-" + neiC)){
                    continue;
                }
                visited.add(neiR + "-" + neiC);
                int maxT = Math.max(t, grid[neiR][neiC]);
                minH.offer(new int[]{maxT, neiR, neiC});
            }
        }
        return -1;
    }
}