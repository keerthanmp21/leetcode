from typing import List
from collections import deque

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        
        def dfs(r,c):
            if(r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or (r,c) in visit):
                return True
            visit.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False
            res = dfs(r-1,c) and res
            res = dfs(r+1,c) and res
            res = dfs(r,c-1) and res
            res = dfs(r,c+1) and res
            return res
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    count += 1
                    
        return count
    
    # bfs
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        count = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            flag = True
            while q:
                row, col = q.popleft()
                if grid1[row][col] == 0:
                    flag = False
                for d in directions:
                    dr = row + d[0]
                    dc = col + d[1]
                    if(dr in range(ROWS) and dc in range(COLS) and (dr,dc) not in visit and grid2[dr][dc] == 1):
                        visit.add((dr,dc))
                        q.append((dr,dc))

            return flag

        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 1 and (r,c) not in visit and bfs(r,c):
                    count += 1
        return count
        
