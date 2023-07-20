from typing import List
from collections import deque

class Solution:
    # bfs
    # tc O(ROWS*COLS), sc O(ROWS*COLS)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        def bfs(r,c):
            if r<0 or r>ROWS-1 or c<0 or c>COLS-1 or mat[r][c]==0 or (r,c) in visit:
                return
            q.append([r,c])
            visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                mat[r][c] = dist
                bfs(r-1,c)
                bfs(r+1,c)
                bfs(r,c-1)
                bfs(r,c+1)
            dist +=1 
        return mat
    
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        # bfs
        ROWS, COLS = len(mat), len(mat[0])
        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        dist = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                mat[r][c] = dist
                for d in directions:
                    dr = r+d[0]
                    dc = c+d[1]
                    if (dr<0 or dr==ROWS) or (dc<0 or dc==COLS) or (dr,dc) in visit or mat[dr][dc] == 0:
                        continue
                    q.append((dr,dc))
                    visit.add((dr,dc))
            dist += 1

        return mat
                