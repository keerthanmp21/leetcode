from typing import List
from collections import deque

class Solution:
    # dfs
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maxValue = [0]

        def dfs(r,c,preValue):
            if r<0 or r==ROWS or c<0 or c==COLS or matrix[r][c]<=preValue:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            for d in directions:
                res = max(res,1+dfs(r+d[0],c+d[1],matrix[r][c]))
            dp[(r,c)] = res
            maxValue[0] = max(maxValue[0],res)
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return maxValue[0]
    
    # bfs (tle)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        if ROWS == 1 and COLS == 1:
            return 1

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            res = 0
            while q:
                res += 1
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for d in directions:
                        dr, dc = row+d[0], col+d[1]
                        if(dr<0 or dr==ROWS) or (dc<0 or dc==COLS) or matrix[dr][dc] > matrix[r][c]:
                            continue
                        q.append((dr,dc))
            return res

        maxValue = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxValue = max(maxValue, bfs(r,c))
        return maxValue
    
    # topological sort (bfs)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # idea, use topological sort, search around to find the # of incoming nodes, start with zero indegree with queue, pop from queue, search around and reduce the indegree by 1; push to queue if indegree is 0. output the steps. Time O(mn) and Space O(mn).
        if not matrix:
            return 0
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        cache = {}
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                cnt = 0
                for d in directions:
                    dr, dc = r+d[0], c+d[1]
                    if(0 <= dr < ROWS) and (0 <= dc < COLS) and matrix[dr][dc] < matrix[r][c]:
                        cnt += 1
                cache[(r,c)] = cnt# map point to the # of incoming degree
                if cnt == 0:
                    q.append((r,c))

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    dr, dc = r+d[0], c+d[1]
                    if(0 <= dr < ROWS) and (0 <= dc < COLS) and matrix[dr][dc] > matrix[r][c] and (r,c) in cache:
                        cache[(dr,dc)] -= 1
                        if cache[(dr,dc)] == 0:
                            q.append((dr,dc))
            res += 1
        
        return res

