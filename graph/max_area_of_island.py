from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        self.visited = set()
        maxSize = 0

        for r in range(self.ROWS):
            for c in range(self.COLS):
                size = self.dfs(r, c, grid)
                maxSize = max(maxSize, size)
        
        return maxSize


    def dfs(self, r, c, grid):
        if (r < 0 or r == self.ROWS) or (c < 0 or c == self.COLS) or (r, c) in self.visited or grid[r][c] == 0:
            return 0
        self.visited.add((r, c))
        size = 1
        for d in self.directions:
            size += self.dfs(r + d[0], c + d[1], grid)
        return size
    
    # bfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxSize = 0
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        def bfs(r,c):
            if (r < 0 or r == ROWS) or (c < 0 or c == COLS) or (r, c) in visited or grid[r][c] == 0:
                return 0
            q = deque()
            q.append((r, c))
            size = 1
            while q:
                r,c = q.popleft()
                visited.add((r, c))
                for d in directions:
                    size += bfs(r + d[0], c + d[1])
                
            return size

        maxSize = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxSize = max(maxSize, bfs(r,c))

        return maxSize

