from typing import List
from collections import deque


class Solution:
    # dfs
    # tc O(m*n), sc O(m*n)
    def pacificAtlantic1(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

    # bfs
    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = []
        atlantic = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        def bfs(l):
            q = deque(l)
            visit = set(l)
            while q:
                r, c = q.popleft()
                for d in directions:
                    dr = r + d[0]
                    dc = c + d[1]
                    if (
                        (0 <= dr < ROWS)
                        and (0 <= dc < COLS)
                        and (dr, dc) not in visit
                        and heights[dr][dc] >= heights[r][c]
                    ):
                        visit.add((dr, dc))
                        q.append((dr, dc))
            return visit

        return list(bfs(pacific) & bfs(atlantic))
