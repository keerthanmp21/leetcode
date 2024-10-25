from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N
        visit = set()
        def dfs(r, c):
            if(invalid(r, c) or not grid[r][c] or (r, c) in visit):
                return 
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr,c + dc)
                
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:# reached 2nd island
                            return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                res += 1
                        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c) # get one island cells in visit
                    # in bfs we check from which island cell we get shortest path to other island
                    return bfs()

'''
The `shortestBridge` function is designed to find the shortest path to connect two 
islands in a binary grid. Let’s analyze its time and space complexity:

### Time Complexity:
1. **DFS for Island Identification**:
   - The DFS function explores all cells of one island. In the worst case, this could 
   visit all \(N^2\) cells of the grid, where \(N\) is the number of rows or columns.
   - Thus, the time complexity for the DFS step is \(O(N^2)\).

2. **BFS for Shortest Path**:
   - After identifying one island, the BFS is initiated. The BFS could also potentially 
   visit all cells in the grid, and for each cell, it checks its 4 neighbors.
   - Therefore, the time complexity for the BFS step is also \(O(N^2)\).

3. **Overall Time Complexity**:
   - Since both the DFS and BFS could run independently through all \(N^2\) cells, 
   the overall time complexity is:
   \[
   O(N^2)
   \]

### Space Complexity:
1. **Visited Set**: 
   - The `visit` set stores cells of one island and possibly additional cells during 
   the BFS. In the worst case, it could contain up to \(N^2\) cells.
   - Therefore, the space complexity due to the visited set is \(O(N^2)\).

2. **Queue for BFS**:
   - The BFS uses a queue that can also hold up to \(O(N^2)\) cells at once in the 
   worst case.
   
3. **Overall Space Complexity**:
   - Thus, the overall space complexity is:
   \[
   O(N^2)
   \]

### Summary:
- **Time Complexity**: \(O(N^2)\)
- **Space Complexity**: \(O(N^2)\)
''' 