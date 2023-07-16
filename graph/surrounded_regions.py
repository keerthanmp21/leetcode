from typing import List
from collections import deque

class Solution:
    # dfs
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or board[r][c]!='O':
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # 1. (DFS) Capture unsurrounded regions (O -> T) 
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0,ROWS-1] or c in [0,COLS-1]) and board[r][c] == 'O':
                    dfs(r,c)

        # 2. Capture surrounded regions (O -> X)      
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
    
    # bfs
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque([])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0,ROWS-1] or c in [0,COLS-1]) and board[r][c] == 'O':
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()
            if 0<=r<ROWS and 0<=c<COLS and board[r][c] == 'O':
                board[r][c] = 'T'
                q.extend(((r+1,c),(r-1,c),(r,c+1),(r,c-1)))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                