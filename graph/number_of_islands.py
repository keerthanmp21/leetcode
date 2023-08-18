from typing import List
from collections import deque

class Solution:
    # dfs
    # tc O(m*n), sc O(m*n)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                grid[r][c] != '1' or
                (r,c) in visited):
                return
            visited.add((r,c))
            for d in directions:
                dfs(r+d[0],c+d[1])

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)

        return islands
        
    # bfs
    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            q.append([r,c])
            while q:
                r,c = q.popleft()
                if (r in range(ROWS) and
                c in range(COLS) and
                grid[r][c] == '1' and
                (r,c) not in visited):
                    visited.add((r,c))
                    for d in directions:
                        q.append([r+d[0], c+d[1]])

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)

        return islands