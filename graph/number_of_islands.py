from typing import List
from collections import deque

class UnionFind:
    def __init__(self, total_elements):
        self.parent = list(range(total_elements))
        self.rank = [1] * total_elements
        self.count = 0  # Tracks number of islands

    def find(self, x):
        while x != self.parent[x]:  # Iterative path compression
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1  # Merge islands, reduce count

class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if(r not in range(ROWS) or c not in range(COLS) or
            grid[r][c] != '1' or (r, c) in visited):
                return
            visited.add((r, c))
            for d in directions:
                dr, dc = r + d[0], c + d[1]
                dfs(dr, dc)


        for r in range(ROWS):
            for c in range(COLS):
                if((r, c) not in visited and grid[r][c] == '1'):
                    islands += 1
                    dfs(r, c)

        return islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(row, col):
            q = deque()
            q.append([row, col])
            while q:
                r, c = q.popleft()
                if(r in range(ROWS) and c in range(COLS) and
            grid[r][c] == '1' and (r, c) not in visited):
                    visited.add((r, c))
                    for d in directions:
                        q.append([r + d[0], c + d[1]])

        for r in range(ROWS):
            for c in range(COLS):
                if((r, c) not in visited and grid[r][c] == '1'):
                    islands += 1
                    bfs(r, c)

        return islands

    def numIslands(grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        uf = UnionFind(ROWS * COLS)

        # Count initial number of islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    uf.count += 1  # Every '1' is initially an island

        # Union adjacent land cells
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    index = r * COLS + c
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                            uf.union(index, nr * COLS + nc)

        return uf.count  # Number of connected components