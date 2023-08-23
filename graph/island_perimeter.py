from typing import List
from collections import deque


class Solution:
    # dfs
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i, j))
            perim = dfs(i, j + 1)
            perim += dfs(i, j - 1)
            perim += dfs(i + 1, j)
            perim += dfs(i - 1, j)
            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

    # bfs
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visitSet = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        perims = [0]

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visitSet.add((row, col))

            while q:
                r, c = q.popleft()
                for d in directions:
                    dr, dc = r + d[0], c + d[1]
                    if (dr < 0 or dr == ROWS) or (dc < 0 or dc == COLS):
                        perims[0] += 1
                    elif grid[dr][dc] == 0:
                        perims[0] += 1
                    elif grid[dr][dc] and (dr, dc) not in visitSet:
                        visitSet.add((dr, dc))
                        q.append((dr, dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visitSet:
                    bfs(r, c)

        return perims[0]
